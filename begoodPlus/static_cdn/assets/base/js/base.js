/* tasks management */
const myStorage = window.sessionStorage;
/*
function getClientTasks() {
    var tasks = myStorage.getItem('tasks');
    if (tasks == undefined) {
        return undefined;
    } else {
        return JSON.parse(tasks);
    }
}

function getClientTask(taskName) {
    var tasks = getClientTasks();
    return tasks[taskName];
}

function setClientTask(taskName, taskData) {
    var tasks = getClientTasks();
    if (tasks == undefined) {
        tasks = {}
    }
    tasks[taskName] = taskData;
    myStorage.setItem('tasks', JSON.stringify(tasks));
    displayTasks();
}

function deleteClientTask(taskName) {
    var tasks = getClientTasks();
    delete tasks[taskName]
    myStorage.setItem('tasks', JSON.stringify(tasks));
    displayTasks();
}*/


/* ================= icon bar functionality start ======================== */
var lastKnownScrollPosition = 0;
var ticking = false;
var side_icons = document.querySelectorAll('.icon-bar .icon');
var is_delivery_first_open = false;
function handleSideIcons(scrollPos) {
    //var icons = document.querySelectorAll('.icon-bar > div');
    if (scrollPos > 200) {
        //
        //var icons = document.querySelectorAll('.icon-bar > div');
        for(var i= 0; i  < side_icons.length; i++) {
            //icons[i].style.transform =  'translateX(0px)';
            side_icons[i].classList.remove('hide');
            side_icons[i].classList.add('pick');
            

        }
        if(is_delivery_first_open == false) {
            var delivery = document.querySelector('.icon-bar .icon.delivery');
            delivery.classList.remove('pick');
            delivery.classList.add('show');
            setTimeout(pick_delivery_icon_in_start, 3000, delivery);
            is_delivery_first_open = true;
        }
    }else {
        
        for(var i= 0; i  < side_icons.length; i++) {
            //icons[i].style.transform =  'translateX(-220px)';
            side_icons[i].classList.remove('show');
            side_icons[i].classList.remove('pick');
            side_icons[i].classList.add('hide');
        }
        //document.querySelector('.icon-bar > div').css('transform', 'translateX(-220px)');
    }
}

function pick_delivery_icon_in_start(delivery) {
    delivery.classList.remove('show');
    delivery.classList.add('pick');
    //is_delivery_first_open = false;
}
document.addEventListener('scroll', function(e) {
    lastKnownScrollPosition = window.scrollY;
    console.log(lastKnownScrollPosition);
    if (!ticking) {
        window.requestAnimationFrame(function() {
          handleSideIcons(lastKnownScrollPosition);
          ticking = false;
        });
    
        ticking = true;
    }
});


for(var i = 0; i < side_icons.length; i++) {
    side_icons[i].addEventListener('click', (event)=> {
        console.log('show');
        debugger;
        if(event.currentTarget.classList.contains('show')) {
            event.currentTarget.classList.remove('show');
        }else {
            event.currentTarget.classList.add('show');
        }
    });
    
}

/* ================= icon bar functionality end ======================== */

function set_autosave(selector, autosave_identifier) {
    if (sessionStorage.getItem(autosave_identifier)) {
        selector.value = sessionStorage.getItem(autosave_identifier);
    }
    selector.addEventListener("change", function () {
        autosave_functionality(autosave_identifier, selector);
    });
}

function autosave_functionality(autosave_identifier, selector) {
    sessionStorage.setItem(autosave_identifier, selector.value);
    console.log(autosave_identifier + ' saved: ' + selector.value);
}


function setContactFormAutoSave() {
    setFormAutoSave($('#contact-form'));
}
function setFormAutoSave(formSelector) {
    frm = formSelector;
    var taskName = frm.find('#taskName').val();

    for (var i = 2; i < frm[0].length; i++) {
        set_autosave(frm[0][i], taskName + '_' + frm[0][i].id);
    }
}

function resetFormAutoSave(formSelector) {
    frm = formSelector;
    var taskName = frm.find('#taskName').val();

    for (var i = 2; i < frm[0].length; i++) {
        sessionStorage.setItem(taskName + '_' + frm[0][i].id, '')
    }
}
function resetContactFormAutoSave() {
    resetFormAutoSave($('#contact-form'));
}
/** contact form submit */
/* TODO: this function dose not clean the autosave data... */
/*
function submitForm() {
    console.log('send form');
    var frm = $('#contact-form');
    var formIsFull = true;
    frm[0].reportValidity();
    frm.find('input').each(function () {
        if ($(this).prop('required') && $(this).val() == '') {
            console.log('form is not full');
            formIsFull = false;
        } else {
            console.log('field full');
        }
    });
    if (!formIsFull) {
        return false;
    }
    frm.submit(); // Submit the form
    var taskName = frm.find('#taskName').val();
    for (var i = 2; i < frm[0].length; i++) {
        $(frm[0][i]).val('');
        $(frm[0][i]).change();
        $(frm[0][i]).trigger('change');
        autosave_functionality(taskName + '_' + frm[0][i].id, frm[0][i]);
    }
    
    frm.reset(); // Reset all form data
    return false; // Prevent page refresh
}*/

/* set tasks in navbar: */
/*
function displayTasks() {
    var dropMenu = $('.navbar .dropdown .dropdown-menu');
    var tasks = getClientTasks();
    if (tasks != undefined) {
        var markup = ``;
        var keys = Object.keys(tasks);
        for (var i = 0; i < keys.length; i++) {

            markup += `<li><a class="dropdown-item" onclick="${tasks[keys[i]].onclick}" href="${tasks[keys[i]].url}">${tasks[keys[i]].msg}</a></li>`
        }
        dropMenu.empty();
        dropMenu.html(markup);
    }
}*/

$(function () {
    $(document).ready(function () {
        if (window.location.hash == '#contact-form') {
            setTimeout(() => {
                window.scrollTo(0, document.body.scrollHeight);
            }, 500);
        }

        getUserTasks();
    });
});

function startGetUserTasksLoop() {
    setInterval(getUserTasks, 15000);
}
function taskClicked(taskName, taskUrl, msg) {
    if(taskUrl !=  window.location.pathname) {
        myStorage.setItem('user_click_task', `${taskName}`);
        window.location.href= taskUrl;
    }else {
        activateUserTask(taskName)
    }
}

function getUserTasks() {
    $.ajax({
        url: "/tasks/get-user-tasks",
        type: "GET",
        //cache:false,
        dataType: "json",
        success: function (json) {
            data = json;
            var markup = ``;
            /*
            for (var i = 0; i < data.length; i++) {
                if (data[i].task_name == "catalog-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="myStorage.setItem('user_click_task', '${data[i].task_name}');" data-task="${data.taskName}" href="/testCatalog#contact-form">לא סיימתי למלא טופס בדף הקטלוג </a></li>`
                } else if (data[i].task_name == "main-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="myStorage.setItem('user_click_task', '${data[i].task_name}');" data-task="${data.taskName}" href="/test#contact-form">לא סיימתי למלא טופס בדף הבית </a></li>`
                } else if (data[i].task_name == "products-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="myStorage.setItem('user_click_task', '${data[i].task_name}');" data-task="${data.taskName}" href="/testCatalog">לחץ כאן לשליחת טופס מוצרים אהובים </a></li>`
                }
            }*/
            for (var i = 0; i < data.length; i++) { 
                if(data[i].task_name == "catalog-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="taskClicked('${data[i].task_name}', '/testCatalog#contact-form', 'לא סיימתי למלא טופס בדף הקטלוג');">לא סיימתי למלא טופס בדף הקטלוג</li>`
                }else if (data[i].task_name == "main-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="taskClicked('${data[i].task_name}', '/test/#contact-form', 'לא סיימתי למלא טופס בדף הבית');">לא סיימתי למלא טופס בדף הבית</li>`
                }else if (data[i].task_name == "products-ec6bb117-c8fa-4a38-989a-ab0e0805e44e") {
                    markup += `<li><a class="dropdown-item" onclick="taskClicked('${data[i].task_name}', '/testCatalog', 'לחץ כאן לשליחת טופס מוצרים אהובים');">לחץ כאן לשליחת טופס מוצרים אהובים</li>`
                }
            }
            $('#navbarDropdownList').html(markup);
            var tasksLenght = $('#navbarDropdownList li').length;
            el = document.getElementById('navbarDropdown');
            var count = Number(el.getAttribute('data-count')) || 0;
            
            if(count != tasksLenght) {
                
                el.setAttribute('data-count', tasksLenght);
                el.classList.remove('notify');
                el.offsetWidth = el.offsetWidth;
                el.classList.add('notify');
            }
            /*
            if (count === 0) {
                el.classList.remove('show-count');
            }else {
                
                el.classList.add('show-count');
            }*/
        },
        error: function (e) {
            console.log('error: ', e);
        }
    });
}


setContactFormAutoSave();
//displayTasks();
startGetUserTasksLoop();