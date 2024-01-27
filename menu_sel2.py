def get_menu():  # used to display a menu
    menu_dict = {
        '1': 'apple',
        '2': 'bananas',
        '3': 'cherries',
        '4': 'pears',
        'X': 'done_ordering'
    }
    return menu_dict

def display_menu(menu_dict):
    for items, values in menu_dict.items():
        print(items + "." + values.replace('_', ' ').capitalize())
    menu_selection = input("What would you like to buy? ").upper()

    if menu_selection not in menu_dict:
        print("Sorry, but that is not an option")
        return display_menu(menu_dict)  # Prompt again for a valid selection
    else:
        print("You selected {}".format(menu_dict[menu_selection]))
        return menu_selection

def display_purchases(items_list):
    if len(items_list) > 0:
        del items_list[-1]
        print("You purchased {} item(s):".format(len(items_list)))
        print(*items_list, sep=", ")
    else:
        print("You haven't purchased any items yet.")

def main():
    menu_selection = ''
    items_list = []
    while menu_selection != 'X':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)
        if menu_selection != 'X':
            items_list.append(menu_dict[menu_selection])
        input("Hit Enter to Continue!!")

    display_purchases(items_list)

if __name__ == '__main__':
    main()
