# Unit4-02/usr/bin/env python3
# This program was created by Larry Nkengbeza
# This program was created on December 2020
# This program multiplies up to users inputed number


def main():
    loop_counter = 0
    # input
    positive_integer = int(input("Enter a number which will be factored: "))
    print("")

    # process and output
    multiplication = positive_integer * loop_counter

    while loop_counter < positive_integer:
        print("{1} * {1} = {0}".format(loop_counter, multiplication))
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
