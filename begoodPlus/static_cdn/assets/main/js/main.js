var carousel = document.querySelector('.carousel');
var cells = carousel.querySelectorAll('.carousel__cell');
var cellCount; // cellCount set from cells-range input value
var selectedIndex = 0;
var cellWidth = carousel.offsetWidth;
var cellHeight = carousel.offsetHeight;
var isHorizontal = true;
var rotateFn = isHorizontal ? 'rotateY' : 'rotateX';
var radius, theta;
// console.log( cellWidth, cellHeight );

function rotateCarousel() {
  var angle = theta * selectedIndex * -1;
  carousel.style.transform = 'translateZ(' + -radius + 'px) ' + 
    rotateFn + '(' + angle + 'deg)';
  console.log(selectedIndex);
  console.log(cells.length);
  console.log(selectedIndex % cells.length);
  for(var i = 0; i< cells.length;i++) {
    cells[i].classList.remove('active');
  }
  cells[selectedIndex % cells.length].classList.add('active');
  //cells.classList.remove('active');

  /*
  cells[(selectedIndex+1) % cells.length].classList.remove('active');
  if((selectedIndex % cells.length)!=0) {
    cells[(selectedIndex % cells.length)-1].classList.remove('active');
  }*/
}

var prevButton = document.querySelector('.previous-button');
prevButton.addEventListener( 'click', function() {
  selectedIndex--;
  rotateCarousel();
});

var nextButton = document.querySelector('.next-button');
nextButton.addEventListener( 'click', function() {
  selectedIndex++;
  rotateCarousel();
});

var cellsRange = document.querySelector('.cells-range');
cellsRange.addEventListener( 'change', changeCarousel );
cellsRange.addEventListener( 'input', changeCarousel );



function changeCarousel() {
  cellCount = cellsRange.value;
  theta = 360 / cellCount;
  var cellSize = isHorizontal ? cellWidth : cellHeight;
  radius = Math.round( ( cellSize / 2) / Math.tan( Math.PI / cellCount ) );
  for ( var i=0; i < cells.length; i++ ) {
    var cell = cells[i];
    if ( i < cellCount ) {
      // visible cell
      cell.style.opacity = 1;
      var cellAngle = theta * i;
      cell.style.transform = rotateFn + '(' + cellAngle + 'deg) translateZ(' + radius + 'px)';
    } else {
      // hidden cell
      cell.style.opacity = 0;
      cell.style.transform = 'none';
    }
  }

  rotateCarousel();
}

var orientationRadios = document.querySelectorAll('input[name="orientation"]');
( function() {
  for ( var i=0; i < orientationRadios.length; i++ ) {
    var radio = orientationRadios[i];
    radio.addEventListener( 'change', onOrientationChange );
  }
})();

function onOrientationChange() {
  var checkedRadio = document.querySelector('input[name="orientation"]:checked');
  isHorizontal = checkedRadio.value == 'horizontal';
  rotateFn = isHorizontal ? 'rotateY' : 'rotateX';
  changeCarousel();
}
var isCaruselLooping;
function initLoopCarusel() {
  isCaruselLooping = true;
  setInterval(() => {
    console.log('set interval');
    loopCarusel()
  }, 500);

  var isHoverd = false;
  $('.scene-wraper').mouseenter( ()=>{
    isCaruselLooping=false;
    } 
    ).mouseleave( ()=>{
      isCaruselLooping=true
    } );

}

function loopCarusel() {
  if(isCaruselLooping) {
    /*const regex1 = 'rotate.\((?:.+?)deg\)/g';
    const startIndex = carousel.style.transform .indexOf('rotate') + 8
    const endIndex = carousel.style.transform .indexOf('deg', startIndex);
    var newRotation = parseInt(carousel.style.transform .substring(startIndex, endIndex));
    //console.log(theta * newRotation * -1);
    carousel.style.transform = 'translateZ(' + -radius + 'px) ' + 
          rotateFn + '(' + (newRotation+10) + 'deg)';

    activeIndex = parseInt(newRotation%360 /theta);
    selectedIndex = cells.length -  activeIndex;
    console.log(cells.length - activeIndex);*/

  }
  /*if(isCaruselLooping) {
    $('.next-button').click();
    console.log('next click');
  }*/
}


document.addEventListener('touchstart', handleTouchStart, false);
var xDown = null;
var yDown = null;

function getTouches(evt) {
  return  evt.touches || // browser API
          evt.originalEvent.touches; // jQuery
}
function handleTouchStart(evt) {
  console.log('handleTouchStart');
  const firstTouch = getTouches(evt)[0];
  xDown = firstTouch.clientX;
  yDown = firstTouch.clientY;
};


$('.scene-wraper').bind('touchmove', function (evt) {
  evt.preventDefault();
  if (!xDown || !yDown) {
    return;
  }

  var xUp = evt.touches[0].clientX;
  var yUp = evt.touches[0].clientY;

  var xDiff = xDown - xUp;
  var yDiff = yDown - yUp;

  if (Math.abs(xDiff) > Math.abs(yDiff)) {
    //most significant
    console.log('xDiff', xDiff, isSwipeInCD());
    if(isSwipeInCD() == false) {
      if (xDiff > 50 ) {
        // left swipe 
        //evt.originalEvent.dataTransfer.setData('d', 'n');
        $('.next-button').click();
        setSwipeCD();
      } else if(xDiff < -50){
        //evt.originalEvent.dataTransfer.setData('d', 'p');
        $('.previous-button').click();
        setSwipeCD();
        // right swipe 
      }
    }
  }
  //var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0];
  //console.log(touch.pageX);
});

const swipeCooldown = 250
var swipeCD = false;
function setSwipeCD() {
  swipeCD = true;
  setTimeout(()=>{swipeCD = false;}, swipeCooldown);
}
function isSwipeInCD() {
  return swipeCD;
}

function setCatalogTaskListiner() {
  var frm = $('.contact-form');
  frm.change(function(){
    console.log('updateMainTask');
    updateMainTask();
  });
}
function updateMainTask(isSubmited=false) {
  var frm = $('.contact-form');
  task_id = myStorage.getItem('task_main_id');
  var serTaskId ='';
  if(task_id) {
    var serTaskId = `&task_id=${task_id}&submited=${isSubmited}`
  }
  serFrm = frm.serialize() + serTaskId;
  
  if(isSubmited) {
    isValid = frm.get(0).reportValidity();
    if(isValid == false) {
      alert('שם ופאלפון הם שדות חובה');
      return;
    }
  }


  $.ajax({
    type: "POST",
    url: '/tasks/update-contact-form',
    data: serFrm,
    success: (json)=> {
      console.log(json);
      myStorage.setItem('task_main_id',json.task_id )
      if (json.task_id == -1) {
        frm.trigger("reset");
        resetContactFormAutoSave();
      }
      getUserTasks();
    },
    dataType: "json"
  });
}
function submitMainContactForm() {
  debugger;
  updateMainTask(isSubmited=true);
}

// set initials
onOrientationChange();
initLoopCarusel();
setCatalogTaskListiner();
getUserTasks();

/*function submitMainContactForm() { 
  var frm = $('.contact-form');
  task_id = myStorage.getItem('task_main_id');
  var serTaskId ='';
  if(task_id) {
    var serTaskId = '&task_id=' + task_id + '&submited=True'
  }
  serFrm = frm.serialize() + serTaskId;
  console.log('serFrm', serFrm);
  $.ajax({
    type: "POST",
    url: '/tasks/submit-contact-form',
    data: serFrm,
    success: (json)=> {
      console.log(json);
      //myStorage.setItem('task_main_id',json.task_id )
      myStorage.removeItem('task_main_id');
      getUserTasks();
    },
    dataType: "json"
  });
}*/
/*
function checkMainTask() {
  debugger;
  if(document.querySelector('.contact-form #id_name').value != "" ||
     document.querySelector('.contact-form #id_phone').value != "" || 
     document.querySelector('.contact-form #id_email').value != "" || 
     document.querySelector('.contact-form #id_message').value != "") {
    setClientTask('main', {
      'msg':'לא סיימת למלא טופס יצירת קשר בדף הראשי',
      'url': '/test#contact-form'
    });
  }else {
    deleteClientTask('main');
  }
}
*/

/**base */
