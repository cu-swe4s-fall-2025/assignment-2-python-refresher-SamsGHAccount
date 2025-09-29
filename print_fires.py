import argparse
import my_utils as mu

#Adds the different arguments, if they're required, and defaults.
def main():
    parser = argparse.ArgumentParser(description="Returns a column of data for specific country.")
    parser.add_argument('--file', type=str, required=True, help='CSV file name')
    parser.add_argument('--country', type=str, required=True, help='Country to search')
    parser.add_argument('--county_column', type=int, default=0, help='Index for country name')
    parser.add_argument('--return_col', type=int, required=True, help='Index to return')
    parser.add_argument('--info_ret', type=str, required=False, help='Info to return')

    args = parser.parse_args()

    try:
        return_raw = mu.get_column(args.file, args.county_column, args.country, args.return_col, args.info_ret)

        print (return_raw)

    #returns an error when the file isn't found
    except FileNotFoundError:
        print("Could not find file " + args.file)
    #returns an error when the program isn't allowed to access the file
    except PermissionError:
        print("Not allowed to access " + args.file)
    #returns an error when the program can't convert the values to integers
    except ValueError:
        print("Could not convert values to integers!")
    #returns a broad error
    except Exception:
        print("Uh-oh! Something unexpected happened!")

if __name__ == "__main__":
    main()