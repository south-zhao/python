from tkinter import Tk, Label, Entry, Button, Listbox, messagebox


class Student:
    def __init__(self, name, student_id, major, credit):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.credit = credit


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("学生管理系统")

        self.label_name = Label(root, text="姓名:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_id = Label(root, text="学号:")
        self.label_id.grid(row=1, column=0, padx=10, pady=10)
        self.entry_id = Entry(root)
        self.entry_id.grid(row=1, column=1, padx=10, pady=10)

        self.label_major = Label(root, text="专业:")
        self.label_major.grid(row=2, column=0, padx=10, pady=10)
        self.entry_major = Entry(root)
        self.entry_major.grid(row=2, column=1, padx=10, pady=10)

        self.label_credit = Label(root, text="学分:")
        self.label_credit.grid(row=3, column=0, padx=10, pady=10)
        self.entry_credit = Entry(root)
        self.entry_credit.grid(row=3, column=1, padx=10, pady=10)

        self.button_add = Button(root, text="添加学生", command=self.add_student)
        self.button_add.grid(row=4, column=0, padx=10, pady=10)

        self.button_update = Button(root, text="修改学生信息", command=self.update_student)
        self.button_update.grid(row=4, column=1, padx=10, pady=10)

        self.button_delete = Button(root, text="删除选中", command=self.delete_student)
        self.button_delete.grid(row=4, column=2, padx=10, pady=10)

        self.button_display = Button(root, text="显示学生信息", command=self.display_student)
        self.button_display.grid(row=5, column=0, padx=10, pady=10)

        self.button_display_all = Button(root, text="显示所有学生信息", command=self.display_all_students)
        self.button_display_all.grid(row=5, column=1, padx=10, pady=10)

        self.listbox_students = Listbox(root)
        self.listbox_students.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.listbox_students.bind("<<ListboxSelect>>", self.select_student)

        self.students = []

    def add_student(self):
        name = self.entry_name.get()
        student_id = self.entry_id.get()
        major = self.entry_major.get()
        credit = self.entry_credit.get()

        if name and student_id and major and credit:
            student = Student(name, student_id, major, credit)
            self.students.append(student)

            self.listbox_students.insert("end", f"姓名: {name}, 学号: {student_id}, 专业: {major}, 学分: {credit}")

            self.clear_entries()

            with open("student.txt", "a", encoding="utf-8") as f:
                f.writelines(f"{student_id} {name} {major} {credit}")
        else:
            messagebox.showerror("错误", "请输入完整的学生信息")

    def update_student(self):
        selected_index = self.listbox_students.curselection()

        with open("student.txt", "r", encoding="utf-8") as f:
            con = f.readlines()
            con1 = []
            for i in con:
                con1.append(i.split())

        if selected_index:
            student = self.students[selected_index[0]]
            student.name = self.entry_name.get()
            student.student_id = self.entry_id.get()
            student.major = self.entry_major.get()
            student.credit = self.entry_credit.get()

            self.listbox_students.delete(selected_index)

            self.listbox_students.insert(selected_index,
                                         f"姓名: {student.name}, 学号: {student.student_id}, 专业: {student.major}, 学分: {student.credit}")

            self.clear_entries()

    def delete_student(self):
        selected_index = self.listbox_students.curselection()

        if selected_index:
            self.listbox_students.delete(selected_index)
            del self.students[selected_index[0]]
            self.clear_entries()

    def display_student(self):
        selected_index = self.listbox_students.curselection()

        if selected_index:
            student = self.students[selected_index[0]]
            messagebox.showinfo("学生信息",
                                f"姓名: {student.name}\n学号: {student.student_id}\n专业: {student.major}\n学分: {student.credit}")

    def display_all_students(self):
        message = ""
        for student in self.students:
            message += f"姓名: {student.name}, 学号: {student.student_id}, 专业: {student.major}, 学分: {student.credit}\n"
        messagebox.showinfo("所有学生信息", message)

    def select_student(self, event):
        selected_index = self.listbox_students.curselection()

        if selected_index:
            student = self.students[selected_index[0]]
            self.entry_name.delete(0, "end")
            self.entry_name.insert("end", student.name)
            self.entry_id.delete(0, "end")
            self.entry_id.insert("end", student.student_id)
            self.entry_major.delete(0, "end")
            self.entry_major.insert("end", student.major)
            self.entry_credit.delete(0, "end")
            self.entry_credit.insert("end", student.credit)

    def clear_entries(self):
        self.entry_name.delete(0, "end")
        self.entry_id.delete(0, "end")
        self.entry_major.delete(0, "end")
        self.entry_credit.delete(0, "end")


if __name__ == "__main__":
    root = Tk()
    student_management_system = StudentManagementSystem(root)
    root.mainloop()
