import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--repete',
                    dest='rep',
                    default=2,
                    help="Nombre de fois que vous souhaitez afficher la chaine",
                    type=int
                    )
parser.add_argument('-c', '--chaine',
                    dest='ch',
                    help="Chaîne que vous souhaitez répéter",
                    type=str,
                    required=True
                    )

args = parser.parse_args()


for i in range(args.rep):
    print(f"{i+1}) {args.ch}")