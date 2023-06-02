
$(document).ready(function(){
  $('.courses-slider').slick({
    dots: true,
    arrows: false,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    centerMode: true,
    variableWidth: true,
    pauseOnHover: true,
    autoplay: true,
    autoplaySpeed: 4000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  // destination page
  $('.courses-slider-2').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    pauseOnHover: true,
    autoplay: true,
    autoplaySpeed: 4000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  $('.dest-slider').slick({
      dots: false,
      infinite: true,
      speed: 300,
      slidesToShow: 3,
      slidesToScroll: 1,
      arrows: true,
      loop: true,
      autoplay: true,
      autoplaySpeed: 4000,
      responsive: [
          {
          breakpoint: 1200,
          settings: {
              slidesToShow: 3,
          }
          },
          {
          breakpoint: 992,
          settings: {
              slidesToShow: 2,
          }
          },
          {
          breakpoint: 768,
          settings: {
              slidesToShow: 1,
          }
          }
      ]
  });

  $('.partners-slider').slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    loop: true,
    centerMode: true,
    autoplay: true,
    autoplaySpeed: 4000,
    responsive: [
        {
        breakpoint: 1480,
        settings: {
            slidesToShow: 3,
        }
        },
        {
          breakpoint: 1200,
          settings: {
              slidesToShow: 2,
          }
          },
        {
        breakpoint: 992,
        settings: {
            slidesToShow: 1,

        }
        }
    ]
  });

  $('.affiliations-slider').slick({
    dots: false,
    infinite: false,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: false,
    loop: true,
    autoplay: false,
    autoplaySpeed: 4000,
    responsive: [
      {
      breakpoint: 1200,
      settings: {
          slidesToShow: 3,
      }
      },
      {
        breakpoint: 992,
        settings: {
            slidesToShow: 2,
        }
        },
      {
      breakpoint: 576,
      settings: {
          slidesToShow: 1,
      }
      }
  ]
  });

  $('.tests-slider').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    loop: true,
    autoplay: true,
    autoplaySpeed: 4000,
  });

  const checkboxBtns = $('.checkbox-btn');
  jQuery.each(checkboxBtns, function(idx, checkboxBtn){
    $(checkboxBtn).click(function(){
      if($(checkboxBtn).is(":checked")){
        console.log(checkboxBtn);
        $(checkboxBtn).parent().addClass('checkbox-item-active');
      } else {
        $(checkboxBtn).parent().removeClass('checkbox-item-active');
      }
    });
  });

  jQuery.each(checkboxBtns, function(idx, checkboxBtn){
    if($(checkboxBtn).is(":checked")){
      console.log(checkboxBtn);
      $(checkboxBtn).parent().addClass('checkbox-item-active');
    }
  });




   // destination page
   $('.criteria-slider').slick({
    arrows: true,
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    pauseOnHover: true,
    autoplay: true,
    autoplaySpeed: 4000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3
        }
      },
      {
        breakpoint: 1080,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });
});

