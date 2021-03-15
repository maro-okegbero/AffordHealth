(function($) {
	'use strict';
	jQuery(document).on('ready', function(){
		
		// Mean Menu
		 jQuery('.mean-menu').meanmenu({
			meanScreenWidth: "991"
        });

		// Preloader
		jQuery(window).on('load', function() {
            $('.preloader').fadeOut();
		});

		// Home Slides
		$('.home-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            animateOut: "slideOutDown",
            animateIn: "slideInDown",
            items: 1,
            navText: [
                "<i class='flaticon-left-chevron'></i>",
                "<i class='flaticon-right-chevron'></i>"
            ]
		});
		
		// Home Slides Two
		$('.home-slides-four').owlCarousel({
			loop: true,
			nav: true,
			dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            animateOut: "fadeOut",
            items: 1,
            navText: [
                "<i class='flaticon-left-chevron'></i>",
                "<i class='flaticon-right-chevron'></i>"
            ]
        });
        $(".home-slides").on("translate.owl.carousel", function(){
            $(".main-banner-content span").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content h1").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content .banner-btn").removeClass("animated fadeInUp").css("opacity", "0");
        });
        $(".home-slides").on("translated.owl.carousel", function(){
            $(".main-banner-content span").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content h1").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content .banner-btn").addClass("animated fadeInUp").css("opacity", "1");
		});

        $(".home-slides-four").on("translate.owl.carousel", function(){
            $(".main-banner-content span").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content h1").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content .banner-btn").removeClass("animated fadeInUp").css("opacity", "0");
        });
        $(".home-slides-four").on("translated.owl.carousel", function(){
            $(".main-banner-content span").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content h1").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content .banner-btn").addClass("animated fadeInUp").css("opacity", "1");
		});

		// Nice Select JS
        $('select').niceSelect();
		
		// Header Sticky
        $(window).on('scroll', function() {
            if ($(this).scrollTop() >150){  
                $('.navbar-area').addClass("is-sticky");
            }
            else{
                $('.navbar-area').removeClass("is-sticky");
            }
		});

		// Banner Image Slider
		$('.banner-image-slider').owlCarousel({
			loop: true,
			nav: true,
			dots: false,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 1
				},
				1200: {
					items: 1
				}
			}
		});
		
		// Sidebar Modal
        $(".burger-menu").on('click',  function() {
			$('.sidebar-modal').toggleClass('active');
		});
        $(".sidebar-modal-close-btn").on('click',  function() {
			$('.sidebar-modal').removeClass('active');
        });
        
        // Search Popup JS
        $('.close-btn').on('click',function() {
            $('.search-overlay').fadeOut();
            $('.search-btn').show();
            $('.close-btn').removeClass('active');
        });
        $('.search-btn').on('click',function() {
            $(this).hide();
            $('.search-overlay').fadeIn();
            $('.close-btn').addClass('active');
        });

		// Popup Video
		$('.popup-youtube').magnificPopup({
			disableOn: 320,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
		});
		
		// Odometer JS
        $('.odometer').appear(function(e) {
			var odo = $(".odometer");
			odo.each(function() {
				var countNumber = $(this).attr("data-count");
				$(this).html(countNumber);
			});
		});
		
		// Tabs
		$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
		$('.tab ul.tabs li a').on('click', function (g) {
			var tab = $(this).closest('.tab'), 
			index = $(this).closest('li').index();
			tab.find('ul.tabs > li').removeClass('current');
			$(this).closest('li').addClass('current');
			tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
			tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
			g.preventDefault();
		});

		// Event Slider
		$('.event-slider').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            margin: 30,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 2
				},
				1200: {
					items: 2
				}
			}
		});
		
		// Testimonials Slider
		$('.testimonials-slider').owlCarousel({
			loop: true,
			nav: true,
			dots: false,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            margin: 30,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 2
				},
				991: {
					items: 1
				},
				1200: {
					items: 1
				}
			}
		});
		
		// Testimonials Slider Two
		$('.testimonials-slider-two').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            margin: 30,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 2
				},
				1200: {
					items: 2
				}
			}
		});
		
		// Feature Slider
		$('.feature-slider').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
			margin: 30,
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 2
				},
				1200: {
					items: 3
				}
			}
        });
		
		// Go to Top
        $(function(){
            // Scroll Event
            $(window).on('scroll', function(){
                var scrolled = $(window).scrollTop();
                if (scrolled > 600) $('.go-top').addClass('active');
                if (scrolled < 600) $('.go-top').removeClass('active');
            });  
            // Click Event
            $('.go-top').on('click', function() {
                $("html, body").animate({ scrollTop: "0" },  500);
            });
		});

		//skill
		jQuery('.skill-bar').each(function() {
			jQuery(this).find('.progress-content, .progress-content-two, .progress-content-three').animate({
			width:jQuery(this).attr('data-percentage')
			},2000);
			
			jQuery(this).find('.progress-number-mark').animate(
			{left:jQuery(this).attr('data-percentage')},
			{
				duration: 2000,
				step: function(now, fx) {
				var data = Math.round(now);
				jQuery(this).find('.percent').html(data + '%');
				}
			});  
		});

		// Feedback Slider
		$('.feedback-slider').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 1000,
            margin: 30,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 1
				},
				768: {
					items: 2
				},
				1200: {
					items: 2
				}
			}
		});

		// Instagram Slides
		$('.instagram-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
			autoplayHoverPause: true,
            smartSpeed: 750,
			autoplay: true,
            navText: [
                "<i class='fas fa-chevron-left'></i>",
                "<i class='fas fa-chevron-right'></i>"
            ],
			responsive: {
                0: {
                    items: 2,
                },
                768: {
                    items: 6,
                },
                1200: {
                    items: 5,
				}
            }
		});

		// Subscribe form
		$(".newsletter-form").validator().on("submit", function (event) {
			if (event.isDefaultPrevented()) {
			// handle the invalid form...
				formErrorSub();
				submitMSGSub(false, "Please enter your email correctly.");
			} else {
				// everything looks good!
				event.preventDefault();
			}
		});
		function callbackFunction (resp) {
			if (resp.result === "success") {
				formSuccessSub();
			}
			else {
				formErrorSub();
			}
		}
		function formSuccessSub(){
			$(".newsletter-form")[0].reset();
			submitMSGSub(true, "Thank you for subscribing!");
			setTimeout(function() {
				$("#validator-newsletter").addClass('hide');
			}, 4000)
		}
		function formErrorSub(){
			$(".newsletter-form").addClass("animated shake");
			setTimeout(function() {
				$(".newsletter-form").removeClass("animated shake");
			}, 1000)
		}
		function submitMSGSub(valid, msg){
			if(valid){
				var msgClasses = "validation-success";
			} else {
				var msgClasses = "validation-danger";
			}
			$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
        }
        // AJAX MailChimp
		$(".newsletter-form").ajaxChimp({
			url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
			callback: callbackFunction
        });
		
		// Popup Image
        $('a[data-imagelightbox="popup-btn"]')
        .imageLightbox({
            activity: true,
            overlay: true,
            button: true,
            arrows: true
		});
		
		// FAQ Accordion
        $(function() {
            $('.accordion').find('.accordion-title').on('click', function(){
                // Adds Active Class
                $(this).toggleClass('active');
                // Expand or Collapse This Panel
                $(this).next().slideToggle('fast');
                // Hide The Other Panels
                $('.accordion-content').not($(this).next()).slideUp('fast');
                // Removes Active Class From Other Titles
                $('.accordion-title').not($(this)).removeClass('active');		
            });
        });

		// Preloader
		jQuery(window).on('load', function () {
			$('#preloader').fadeOut()
		})



	});

})(jQuery);

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

var paymentForm = document.getElementById('paymentForm');
paymentForm.addEventListener('submit', payWithPaystack, false);
function payWithPaystack() {
	console.log('It hit here, hulabalu');
  var handler = PaystackPop.setup({
    key: 'pk_test_0f0c191f5e42b47447ebbfd26e7d188265075ba6', // Replace with your public key
    email: document.getElementById('email-address').value,
    amount: document.getElementById('amount').value * 100, // the amount value is multiplied by 100 to convert to the lowest currency unit
    ref: document.getElementById('reference').value ,
    currency: 'NGN', // Use GHS for Ghana Cedis or USD for US Dollars
    callback: function(response) {
      //this happens after the payment is completed successfully
      var reference = 'ze reference ';
      alert('Payment complete! Reference: ' + reference)
		// Make an AJAX call to your server with the reference to verify the transaction
    },
    onClose: function() {
      alert('Transaction was not completed, window closed.');
    },

  });
  console.log('about to open iframe............')
  handler.openIframe();
  var form = document.getElementById("paymentForm");
  function handleForm(event) { event.preventDefault(); }
  form.addEventListener('submit', handleForm);

}

