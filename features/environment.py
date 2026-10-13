import os
import time
from utils.config_reader import ConfigReader
from utils.driver_factory import DriverFactory


def before_all(context):
    context.config_data = ConfigReader()
    context.base_url = context.config_data.get("base_url")

    browser = context.config_data.get("browser")
    headless = context.config_data.getboolean("headless")

    context.driver = DriverFactory.get_driver(browser=browser, headless=headless)
    context.driver.maximize_window()

    print("\n" + "=" * 72)
    print("  🎯 ShopQA — E-COMMERCE AUTOMATION TEST SUITE")
    print(f"  🌐 Target   : {context.base_url}")
    print(f"  🖥  Browser  : {browser}  |  Headless: {headless}")
    print("=" * 72)


def before_feature(context, feature):
    print("\n\n" + "█" * 72)
    print(f"  📋 FEATURE: {feature.name}")
    if feature.description:
        for line in feature.description:
            stripped = line.strip()
            if stripped:
                print(f"     {stripped}")
    print("█" * 72)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.get(context.base_url)

    print("\n" + "─" * 72)
    print(f"  ▶  SCENARIO: {scenario.name}")
    if scenario.tags:
        print(f"     Tags: {' '.join('@' + t for t in scenario.tags)}")
    print("─" * 72)
    time.sleep(1)


def after_step(context, step):
    icon = "✅" if step.status == "passed" else "❌"
    print(f"     {icon}  {step.keyword} {step.name}")
    time.sleep(1)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("reports/screenshots", exist_ok=True)
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")
        try:
            context.driver.save_screenshot(f"reports/screenshots/{safe_name}.png")
            print(f"\n     📸 Screenshot: reports/screenshots/{safe_name}.png")
        except Exception:
            pass
        print(f"     ❌ SCENARIO FAILED")
    else:
        print(f"     ✅ SCENARIO PASSED")


def after_all(context):
    print("\n\n" + "=" * 72)
    print("  ✅ TEST SUITE COMPLETE")
    print("=" * 72)
    if hasattr(context, "driver"):
        context.driver.quit()