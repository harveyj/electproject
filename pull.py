import urllib,json,argparse

parser=argparse.ArgumentParser()
parser.add_argument("--urls")
args=parser.parse_args()

for l in open(args.urls):
    data = json.loads(urllib.urlopen(l).read())
    for line in data["counties"]:
        out = []
        out.append(line["name"])
        for c in line["race"]["candidates"]:
            out += [c["fname"] + " " + c["lname"], str(c["votes"])]
        print ",".join(out)

