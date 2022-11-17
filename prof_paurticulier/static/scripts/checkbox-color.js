var label_button = document.querySelectorAll("#research_filter div>label");
var label_input = document.querySelectorAll("#research_filter div>label>input");
var delete_filters = document.getElementById("delete_filters");

for (let i = 0; i < label_button.length; i++) {
    if (label_input[i].checked) {
        label_button[i].classList.add("active");
    }
    else {
        label_button[i].classList.remove("active");
    }
};

for (let i = 0; i < label_button.length; i++) {
    label_input[i].addEventListener('click', function (e) {
        // e.preventDefault();
        if (label_input[i].checked) {
            label_button[i].classList.add("active");
        }
        else {
            label_button[i].classList.remove("active");
        }
    });
};

delete_filters.addEventListener('click', function () {
    for (let i = 0; i < label_input.length; i++) {
        label_input[i].checked = false;
    };
});