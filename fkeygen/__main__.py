import argparse

VERSION = "1.0"

def generate_phone_xml(e164_list, idskip_list, pretty):
    output = ""
    indent = "    " if pretty else ""

    for own in e164_list:
        xml_lines = []

        if pretty:
            xml_lines.append("<phone>")
        else:
            xml_lines.append("<phone>")

        id_counter = 0
        for e164 in e164_list:
            if e164 == own:
                continue

            while id_counter in idskip_list:
                id_counter += 1
            line = f"{indent}<f id='{id_counter}'><p e164='{e164}' pr='1' di='1'></p></f>"
            xml_lines.append(line)
            id_counter += 1

        if pretty:
            xml_lines.append("</phone>")
            xml = "\n".join(xml_lines)
        else:
            xml = "".join(xml_lines) + "</phone>"

        output += f"\n### e164={own}\n{xml}\n"

    return output


def main():
    parser = argparse.ArgumentParser(description=f"fkeygen v{VERSION} - XML Generator")
    parser.add_argument("--list", help="E164 list as comma-separated string e.g.: 100,101,102,103,...")
    parser.add_argument("--file", help="Optional output file path", default=None)
    parser.add_argument("--idskip", help="Comma separated list of IDs to skip e.g.: 6,7", default="8")
    parser.add_argument("--pretty", action="store_true", help="Pretty print (multi-line XML)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

    args = parser.parse_args()

    if args.list:
        e164_input = args.list
    else:
        e164_input = input("Enter a comma separated list of numbers: ")

    try:
        e164_list = [int(num.strip()) for num in e164_input.split(",") if num.strip()]
        idskip_list = [int(i.strip()) for i in args.idskip.split(",") if i.strip()]
    except ValueError:
        print("❌ Error: Only numbers are allowed in the list.")
        return

    if len(e164_list) < 2:
        print("❌ Enter atleast two numbers.")
        return

    result = generate_phone_xml(e164_list, idskip_list, args.pretty)

    if args.file:
        with open(args.file, "w") as f:
            f.write(result)
        print(f"✅ XML was saved at '{args.file}'.")
    else:
        print(result)


if __name__ == "__main__":
    main()
