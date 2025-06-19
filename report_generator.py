import argparse
from datetime import date


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate customizable text reports.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--title", default="Untitled Report", help="Report title")
    parser.add_argument("--author", default="Anonymous", help="Author name")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Date to display in the report (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--section",
        action="append",
        default=[],
        help="Sections in the form 'Title:Content'. Can be used multiple times.",
    )
    parser.add_argument(
        "--output",
        default="report.txt",
        help="Path of the generated report file",
    )
    return parser.parse_args()


def parse_sections(section_args):
    sections = []
    for entry in section_args:
        if ":" in entry:
            title, content = entry.split(":", 1)
        else:
            title, content = entry, ""
        sections.append((title.strip(), content.strip()))
    return sections


def generate_report(title, author, report_date, sections):
    lines = [f"# {title}", f"Author: {author}", f"Date: {report_date}", ""]
    for sec_title, sec_content in sections:
        lines.append(f"## {sec_title}")
        if sec_content:
            lines.append(sec_content)
        lines.append("")
    return "\n".join(lines)


def main():
    args = parse_args()
    sections = parse_sections(args.section)
    report = generate_report(args.title, args.author, args.date, sections)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Report generated at {args.output}")


if __name__ == "__main__":
    main()
