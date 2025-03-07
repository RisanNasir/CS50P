
def check_ext(filename):
    filename = filename.lower().strip()

    filter = filename.split(".")
    length = len(filter)
    ext = filter[length-1]

    ## use of switch case

    match ext:
        case "gif" | "png":
            return "image/" + ext
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "pdf" | "zip":
            return "application/" + ext
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"

## use of if elif else
    ##if ext == "gif" or ext == "png":
      ##  return "image/" + ext
    ##elif ext == "jpg" or ext =="jpeg":
      ##  return "image/jpeg"
    ##elif ext == "pdf" or ext == "zip":
      ##  return "application/" + ext
    ##elif ext == "txt":
      ##  return "text/plain"
    ##else:
      ##  return "application/octet-stream"

def main():
    print(check_ext(input("File Name: ")))


main()
