def main():
    nice_list = [
        [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ], 
        [
            [10, 11, 12], 
            [13, 14, 15], 
            [16, 17, 18]
        ]
    ]
    flat_list = [
        elem for sublist1 in nice_list 
             for sublist2 in sublist1 
             for elem in sublist2
    ]
    print(flat_list)

if __name__ == "__main__":
    main()