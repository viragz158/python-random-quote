def test():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  for q in quotes:
    print(q.rstrip("\n"))

if __name__== "__main__":
  test()
