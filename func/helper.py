from func.approximator import approximator
import re


def helper():

    while True:

        list_or_stop = input("\nEnter a list of y values in the format '1 3 12 4' without quotes or 'q' to exit:\n")

        match list_or_stop:

            case 'q':

                print('GoodBye!')

                break

            case _:

                if not all([re.match(r'^-?([1-9][0-9]?|100)$', x) for x in list_or_stop.split()]):

                    print('Invalid input, the maximum value of the value is 100')

                    continue

                if len(list_or_stop.split()) < 4:

                    print('the minimum number of values is 4')

                    continue

                try:

                    file_name = approximator([int(x) for x in list_or_stop.split()])

                except RuntimeError:

                    print('it is difficult to imagine this curve approximated, try adding values or/and increasing '
                          'the gap in values')

                    continue

                except Exception as e:

                    print(f'\nunexpected error:\n\n{e}\n\ntry again')

                    continue

                else:

                    print(f'Successfully, the image is saved at {file_name}')

                    continue
