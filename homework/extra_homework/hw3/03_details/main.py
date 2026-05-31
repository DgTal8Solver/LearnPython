def main():
    shop = [
        ['каретка', 1200], ['шатун', 1000], ['седло', 300], 
        ['педаль', 100], ['седло', 1500], ['рама', 12000], 
        ['обод', 2000], ['шатун', 200], ['седло', 2700]
    ]

    dict_shop = {}
    for name, value in shop:
        if dict_shop.get(name) is None:
            dict_shop[name] = [value]
        else:
            dict_shop[name] += [value]

    detail_name = input("Название детали: ")
    if dict_shop.get(detail_name) is None:
        print("Такой детали нет.")
    else:
        data = dict_shop[detail_name]
        print(f"Кол-во деталей — {len(data)}")
        print(f"Общая стоимость — {sum(data)}")

if __name__ == "__main__":
    main()