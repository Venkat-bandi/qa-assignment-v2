import markdown
import os

def convert(src, dst, title):
    if not os.path.exists(src):
        print(f"⚠️  Skipping (not found): {src}")
        return

    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    body = markdown.markdown(text, extensions=["tables", "fenced_code"])

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 1100px; margin: 32px auto; padding: 0 24px; color: #111827; line-height: 1.6; }}
  h1, h2, h3 {{ color: #4f46e5; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th, td {{ border: 1px solid #e5e7eb; padding: 10px 14px; text-align: left; vertical-align: top; }}
  th {{ background: #f3f4f6; font-weight: 600; }}
  code {{ background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }}
  pre {{ background: #f8fafc; padding: 12px; border-radius: 8px; overflow: auto; }}
  hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 24px 0; }}
</style></head><body>
{body}
</body></html>"""

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {dst}")


if __name__ == "__main__":
    convert("manual_tests/test_cases.md", "reports/test_cases.html", "Test Cases")
    convert("bug_report.md", "reports/bug_report.html", "Bug Report")