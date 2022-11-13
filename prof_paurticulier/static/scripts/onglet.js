ong1 = document.getElementById('a1');
ong2 = document.getElementById('a2');
student = document.getElementById('student');
teacher = document.getElementById('teacher');

function nonactive() {
    ong1.className = "";
    ong2.className = "";
}

function active(self) {
    nonactive();
    self.className = "active";
}

ong1.addEventListener("click", function () {
    student.style.display = "";
    teacher.style.display = "none";
    active(this);
})

ong2.addEventListener("click", function () {
    student.style.display = "none";
    teacher.style.display = "";
    active(this);
})