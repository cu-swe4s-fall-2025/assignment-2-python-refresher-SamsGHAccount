import argparse
import my_utils as mu
def main():
    parser = argparse.ArgumentParser(description="Returns a column of data for specific country.")
    parser.add_argument('--file', type=str, required=True, help='CSV file name')
    parser.add_argument('--country', type=str, required=True, help='Country to search')
    parser.add_argument('--county_column', type=int, default=0, help='Index for country name')
    parser.add_argument('--return_col', type=int, required=True, help='Index to return')

    args = parser.parse_args()

    try:
        return_raw = mu.get_column(args.file, args.county_column, args.country, args.return_col)

        return_int = [int(float(x)) for x in return_raw]

        print(return_int)

    except FileNotFoundError:
        print("Could not find file " + args.file)
    except PermissionError:
        print("Not allowed to access " + args.file)
    except ValueError:
        print("Could not convert values to integers!")
    except Exception:
        print("Uh-oh! Something unexpected happened!")

if __name__ == "__main__":
    main()