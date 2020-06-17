def string_alternative(input):
  return input[::2]

def __main():
    str = input(("Enter Input String:"))
    print("Input string:", str)
    return string_alternative(str)

print("Output string:",__main())