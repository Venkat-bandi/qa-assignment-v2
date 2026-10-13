"""
One-command runner: behave → generate full test-case report.
"""
import subprocess
import sys
import os


def run(cmd):
    print(f"\n▶ {' '.join(cmd)}\n" + "─" * 70)
    subprocess.run(cmd, shell=False)


def main():
    os.makedirs("reports", exist_ok=True)
    os.makedirs("tools", exist_ok=True)

    init_file = os.path.join("tools", "__init__.py")
    if not os.path.exists(init_file):
        open(init_file, "w").close()

    # Behave with JSON — output goes to reports/behave.json
    run([sys.executable, "-m", "behave",
         "--format=json",
         "--outfile=reports/behave.json"])

    # Generate reports
    run([sys.executable, "-m", "tools.generate_report"])

    print("\n" + "=" * 70)
    print("  ✅ DONE — check the reports/ folder")
    print("=" * 70)


if __name__ == "__main__":
    main()