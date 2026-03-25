from parser.pluto_parser import parse_pluto

with open("sample.pluto") as f:
    code = f.read()

result = parse_pluto(code)
print(result)