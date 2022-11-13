ong = document.getElementById('onglet');
student_ong = document.getElementById('a1');
teacher_ong = document.getElementById('a2');
student = document.getElementById('student');
teacher = document.getElementById('teacher');
student_color = getComputedStyle(document.documentElement).getPropertyValue('--main-student-color');
teacher_color = getComputedStyle(document.documentElement).getPropertyValue('--main-teacher-color');

function nonactive() {
    student_ong.className = "";
    teacher_ong.className = "";
}

function active(self) {
    nonactive();
    self.className = "active";
}

student_ong.addEventListener("click", function () {
    student.style.display = "";
    ong.style.borderColor = student_color;
    teacher.style.display = "none";
    active(this);
})

teacher_ong.addEventListener("click", function () {
    student.style.display = "none";
    teacher.style.display = "";
    ong.style.borderColor = teacher_color;
    active(this);
})