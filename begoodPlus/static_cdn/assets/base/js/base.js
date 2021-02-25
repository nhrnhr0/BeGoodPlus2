/* tasks management */
const myStorage = window.sessionStorage;

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
}

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
    frm = $('#contact-form');
    var taskName = frm.find('#taskName').val();

    for (var i = 2; i < frm[0].length; i++) {
        set_autosave(frm[0][i], taskName + '_' + frm[0][i].id);
    }
}


/** contact form submit */
/* TODO: this function dose not clean the autosave data... */
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
    debugger;
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
}

/* set tasks in navbar: */
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
}

$(function () {
    $(document).ready(function () {
        if (window.location.hash == '#contact-form') {
            setTimeout(() => {
                window.scrollTo(0, document.body.scrollHeight);
            }, 500);

            /*$('html, body').animate({
                scrollTop: $(window.location.hash).offset().top + 'px'
            }, 1000, 'swing');*/
        }
    });
});


setContactFormAutoSave();
displayTasks();