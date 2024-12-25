import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    print("Enter the values of the matrix row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Number of columns must match the input.")
            return None
        matrix.append(row)
    return np.array(matrix)

def operations():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        choice = input("Enter your operation (1-6): ")
        
        if choice == "6":
            break

        mat1 = inp_mat("Matrix 1: ")
        
        if mat1 is None:
            print("Error with matrix input. Please try again.")
            continue
        
        if choice == "1":
            mat2 = inp_mat("Matrix 2: ")
            if mat2 is None:
                continue
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 + mat2)
            else:
                print("Matrices should have the same dimensions for addition.")

        elif choice == "2":
            mat2 = inp_mat("Matrix 2: ")
            if mat2 is None:
                continue
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 - mat2)
            else:
                print("Matrices should have the same dimensions for subtraction.")

        elif choice == "3":
            mat2 = inp_mat("Matrix 2: ")
            if mat2 is None:
                continue
            if mat1.shape[1] == mat2.shape[0]:  # Check if multiplication is valid
                print("Result:\n", np.dot(mat1, mat2))
            else:
                print("The number of columns of Matrix 1 should be equal to the number of rows of Matrix 2 for multiplication.")

        elif choice == "4":
            print("Transpose of Matrix 1:\n", mat1.T)

        elif choice == "5":
            if mat1.shape[0] == mat1.shape[1]:  # Only for square matrices
                print("Determinant of Matrix 1:", np.linalg.det(mat1))
            else:
                print("Determinant is only defined for square matrices.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    operations()
