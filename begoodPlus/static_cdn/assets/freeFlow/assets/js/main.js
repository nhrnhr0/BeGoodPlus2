/**
 * Template Name: Regna - v2.2.0
 * Template URL: https://bootstrapmade.com/regna-bootstrap-onepage-template/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */
!(function ($) {
  "use strict";

  // Header fixed and Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
      $('#header').addClass('header-fixed');
    } else {
      $('.back-to-top').fadeOut('slow');
      $('#header').removeClass('header-fixed');
    }
  });

  $('.back-to-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });

  // Mobile Navigation
  if ($('#nav-menu-container').length) {
    var $mobile_nav = $('#nav-menu-container').clone().prop({
      id: 'mobile-nav'
    });
    $mobile_nav.find('> ul').attr({
      'class': '',
      'id': ''
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
    $('body').append('<div id="mobile-body-overly"></div>');
    $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

    $(document).on('click', '.menu-has-children i', function (e) {
      $(this).next().toggleClass('menu-item-active');
      $(this).nextAll('ul').eq(0).slideToggle();
      $(this).toggleClass("fa-chevron-up fa-chevron-down");
    });

    $(document).on('click', '#mobile-nav-toggle', function (e) {
      $('body').toggleClass('mobile-nav-active');
      $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('#mobile-body-overly').toggle();
    });

    $(document).click(function (e) {
      var container = $("#mobile-nav, #mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
      }
    });
  } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
    $("#mobile-nav, #mobile-nav-toggle").hide();
  }
  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 21;
  $(document).on('click', '.nav-menu a, #mobile-nav a, .scrollto', function (e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function () {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.nav-menu, #mobile-nav');

  $(window).on('scroll', function () {
    var cur_pos = $(this).scrollTop() + 200;

    nav_sections.each(function () {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('menu-active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('menu-active');
      }
      if (cur_pos < 300) {
        $(".nav-menu li:first").addClass('menu-active');
      }
    });
  });

  // Porfolio isotope and filter
  /*
  $(window).on('load', function() {
    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function() {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      portfolioIsotope.isotope({
        filter: $(this).data('filter')
      });
      aos_init();
    });
  });

  // Portfolio details carousel
  $(".portfolio-details-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });
*/
  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      once: true
    });
  }
  $(window).on('load', function () {
    aos_init();
    youTubes_makeDynamic();
    initMap();
    //setCurrentLanguage();
  });
  /*
  // Initiate venobox (lightbox feature used in portofilo)
  $(document).ready(function() {
    $('.venobox').venobox();
  });*/

  // jQuery counterUp
  /*
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 1000
  });
*/

  /** youtube video load */
  function youTubes_makeDynamic() {

    var $ytIframes = $('iframe[data-src*="youtube.com"]');
    $ytIframes.each(function (i, e) {
      var $ytFrame = $(e);
      var ytKey;
      //var tmp = $ytFrame.attr('src').split(/\//); 
      var tmp = $ytFrame.data().src.split(/\//);
      tmp = tmp[tmp.length - 1];
      tmp = tmp.split('?');
      ytKey = tmp[0];
      var $ytLoader = $('<div class="ytLoader">');

      $ytLoader.append($('<img class="youtube-cover" src="https://i3.ytimg.com/vi/' + ytKey + '/maxresdefault.jpg">'));
      //$ytLoader.append($('<img class="youtube-cover" src="https://i.ytimg.com/vi/'+ytKey+'/hqdefault.jpg">'));
      $ytLoader.append($('<div class="playBtn"></div>'));
      $ytLoader.data('$ytFrame', $ytFrame);
      $ytFrame.replaceWith($ytLoader);
      $ytLoader.click(function () {
        var $ytFrame = $ytLoader.data('$ytFrame');
        $ytFrame.attr('src', $ytFrame.data().src + '?autoplay=1');
        $ytLoader.replaceWith($ytFrame);
      });
    });
  };

  let map;

  function initMap() {
    var locations = [{
        'name': 'הנסיך הקטן פרחים - ועידת קטוביץ 33, תל אביב יפו',
        'lat': 34.791400,
        'lng': 32.094000,
        'img': 'laLittlePrince.png',
        'url': 'https://lpflowers.co.il/'
      },
      {
        'name': 'דיזיגארדן - דיזנגוף 84, תל־אביב',
        'lat': 34.774680,
        'lng': 32.076730,
        'img': 'dizidarden.jpg',
        'url': 'https://www.instagram.com/dizigarden/'
      },
      {
        'name': 'משתלה אורבנית - רחוב דניאל 27, שוק הכרמל, תל אביב',
        'lat': 34.765190,
        'lng': 32.068180,
        'img': 'urbanPlants.png',
        'url': 'https://mashtela-urbanit.co.il/'
      }
    ];
    /*[
      ['הנסיך הקטן פרחים - ועידת קטוביץ 33, תל אביב יפו', 32.094000, 34.791400],
      [`דיזיגארדן - דיזנגוף 84, תל־אביב`, 32.076730, 34.774680],
      ['משתלה אורבנית - רחוב דניאל 27, שוק הכרמל, תל אביב',  32.068180, 34.765190],
    ]*/

    //https://www.google.com/maps/search/?api=1&query=47.5951518,-122.3316393

    map = new google.maps.Map(document.getElementById("map"), {
      center: {
        lat: 32.073582,
        lng: 34.788052
      },
      zoom: 12,
    });



    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i].lng, locations[i].lat),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function (marker, i) {
        return function () {
          infowindow.setContent(`
        <h5 style="text-align: center;">${locations[i].name}</h5>
        <a href="${locations[i].url}" target=_blank>
        <img style="max-width:450px;padding-left: 25px;" src="static/assets/freeFlow/assets/img/${locations[i].img}"/>
        </a>
        `);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
  }

  /*
  function setCurrentLanguage() {
    var lang_code = document.getElementById('loadedLanguage').value.replace('/', '');
    document.getElementById("languages").value = lang_code;

  }*/

  var language_select = document.getElementById("languages");
  language_select.value = '/freeFlow/' + document.documentElement.lang;
  language_select.addEventListener('change', function (event) {
    var selected_value = this.value;
    window.location = selected_value;
  });



  // translation fits:
  function fitTranslation() {
    var lang = document.documentElement.lang;
    if(lang == 'he') {
      // nav bar
      $('#nav-menu-container').css('transform', 'rotate(180deg)');
      $('#nav-menu-container li').css('transform', 'rotate(-180deg)');

      // about:
      //$('#about .about-container').css('flex-direction', 'row-reverse');
      //$('#about .about-container .icon-box').css('flex-direction', 'row-reverse');
      $('#about > *').css('text-align', 'right');
      $('#about > *').css('direction', 'rtl');
    }
  }

  fitTranslation();
})(jQuery);