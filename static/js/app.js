/*--------------------- Show/Hide Post Settings Function ---------------------*/
function showSettingsMenu(postId) {
  if ($('.SettingMenu-Num'+postId).css('display') == 'none') {
    $('.SettingMenu-Num'+postId).css('display', 'flex');
  }
  else {
    $('.SettingMenu-Num'+postId).css('display', 'none');
  }
};
/*--------------------- Gallery Modal Functions ---------------------*/
var imageIndex = 1;
function setMainImage(index) {
  var galleryImages = $('img[name^="IMG-"]');
  if (index > galleryImages.length) {ndx = 1;imageIndex = 1;}
  else if (index < 1) {ndx = galleryImages.length;imageIndex = galleryImages.length;}
  else {ndx = index;}
  var image    = galleryImages[ndx - 1]
  var srcImage = image.src;
  $('.Main-Image').attr('src', srcImage);
  $('.Main-Image').attr('name', image.name);
  $('.FullSizeImage-Link').attr('href', srcImage);
  var imgReactions = image.name.split('-');
  $('.GoodNum').text(imgReactions[2]);
  $('.AmazingNum').text(imgReactions[3]);
  $('.StarsNum').text(imgReactions[4]);
}
function currentIndex(index) {
  setMainImage(imageIndex = index);
}
function nextImage() {
  setMainImage(imageIndex += 1);
}
function prevImage() {
  setMainImage(imageIndex -= 1);
}
/*----------------------- Make Post Reactions ------------------------*/
function makeGood(elm, post_id) {
  var hostName = window.location.origin;
  var urlAjax  = hostName + "/profiles/posts/good/" + post_id + "/";
  $.getJSON(urlAjax, function(data) {
    if (data.is_action) {
      $(elm).addClass('blue');
      $(elm).addClass('ScaleReaction');
    }
    else {
      $(elm).removeClass('blue');
      $(elm).removeClass('ScaleReaction');
    }
  });
};
function makeAmazing(elm, post_id) {
  var hostName = window.location.origin;
  var urlAjax  = hostName + "/profiles/posts/amazing/" + post_id + "/";
  $.getJSON(urlAjax, function(data) {
    if (data.is_action) {
      $(elm).addClass('red');
      $(elm).addClass('ScaleReaction');
    }
    else {
      $(elm).removeClass('red');
      $(elm).removeClass('ScaleReaction');
    }
  });
};
function makeStar(elm, post_id) {
  true;
}
/*----------------------- Make Image Reactions ------------------------*/

/*--------------------- Delete Image from Gallery ---------------------*/
function deleteImage() {
  var image    = document.getElementsByClassName('Main-Image')[0];
  var idImage  = image.name.split('-')[1];
  var urlAjax  = "delete/" + idImage + "/";
  $.getJSON(urlAjax, function(data) {
    if (data.isDeleted) {
      TemporaryToast('Success', 'Small', 'Top', data.note, 5);
    }
    else {
      TemporaryToast('Error', 'Large', 'Top', data.note, 10);
    }
  });
}
/* ---------------------------------- Toast Functions ------------------------------- */
function CloseableToast(Type, Size, Alignment, Message) {
  var toastElement = "<div class=\"CloseableToast" + " Toast-" + Type + " Toast-" + Size + " Toast-" + Alignment + "\">\
                      <span class=\"CloseToast\">&times;</span> <div class=\"ToastContent\">\
                      <i class=\"" + "" + "\"></i>\
                      <span class=\"ToastText\">" + Message + "</span> </div> </div>";
  $('body').append(toastElement);
  $('.CloseToast').click(function() {
    $('.CloseableToast').remove();
  });
}
function TemporaryToast(Type, Size, Alignment, Message, Seconds) {
  var toastElement = "<div class=\"TemporaryToast " + " Toast-" + Type + " Toast-" + Size + " Toast-" + Alignment + "\">\
                      <div class=\"ToastContent\"> <i class=\"" + "" + "\"></i>\
                      <span class=\"ToastText\">" + Message + "</span> </div> </div>";
  $('body').append(toastElement);
  window.setTimeout(function() {
    $('.TemporaryToast').remove();
  }, Seconds*1000);
}
/* -------------------------- Add Social Media Account Function -------------------------- */
function addSocialMediaAccount(accountType, accountLink) {
  var linkElem = "<div class=\"SocialMedia-Link\"><a target=\"_blank\" href=\"" + accountLink + "\">\
                  <i class=\"fab fa-" + accountType + " " + accountType + "\"></i></a></div>"
  $('.User-Links').append(linkElem);
}
/* ********************************************************************************* */
/* ******************************** jQuery + Ajax ********************************** */
/* ********************************************************************************* */

$(document).ready(function() {
  // Username Validate - if avilable for register new user. --------------------
  $('#id_User_Name').keyup(function() {
    var inputUserName = $('#id_User_Name');
    var userName = inputUserName.val();
    if (userName == '') {
      inputUserName.css('border', '2px solid red');
    }
    var hostName = window.location.origin;
    var urlAjax = hostName +"/authentication/username_validate/" + userName + "/";
    $.getJSON(urlAjax, function(data) {
      if (data.is_available) {
        inputUserName.css('border', '2px solid green');
      }
      else {
        inputUserName.css('border', '2px solid red');
      }
    });
  });
  // Display/Close Share Post Modal --------------------------------------------
  $('.SharePost-Link').click(function() {
    $('.SharePost-Modal').css('display', 'flex');
    $('.Close-SharePostModal').click(function() {
      $('.SharePost-Modal').css('display', 'none');
    })
  });
  // Display/Close Share Image Modal. ------------------------------------------
  $('.ShareImage-Link').click(function() {
    $('.ShareImage-Modal').css('display', 'flex');
    $('.Close-ShareImageModal').click(function() {
      $('.ShareImage-Modal').css('display', 'none');
    })
  });
  // Display/Close Change BIO Modal. -------------------------------------------
  $('.MyBio').click(function() {
    var oldBio = $(this).text();
    $('.ShareBio-txt').text(oldBio);
    $('.ShareBio-Modal').css('display', 'flex');
    $('.Close-BioModal').click(function() {
      $('.ShareBio-Modal').css('display', 'none');
    })
  });
  // Show/Hide Add Link Icon. --------------------------------------------------
  $('.User-Links').hover(
    function() {
      if ($('.SocialMedia-Link').length < 8) {
        $('.AddLink-icon').css('display', 'block');
      }
    },
    function() {
      $('.AddLink-icon').css('display', 'none');
    }
  )
  // Display/Hide Add Link Modal. ----------------------------------------------
  $('.AddLink-icon').click(function() {
    $('.AddLink-Modal').css('display', 'flex');
    $('.Close-AdLinkModal').click(function() {
      $('.AddLink-Modal').css('display', 'none');
    })
  })
  // Add Social Media Link. ----------------------------------------------------
  $('.AddLink-btn').click(function() {
    var socialMediaType = $('.LinkType-select').val();
    var socialMediaLink = "https://" + $('.AddLink-input').val();
    var csrfToken = $('#AddLink-Form').find('input[name=csrfmiddlewaretoken]').val();
    var Data = {
      'Type': socialMediaType,
      'Link': socialMediaLink,
      'csrfmiddlewaretoken': csrfToken
    }
    $.ajax({
      url: 'add_social_media_account/',
      type: 'POST',
      data: Data,
      success: function() {
        $('.AddLink-Modal').css('display', 'none');
        addSocialMediaAccount(socialMediaType.toLowerCase(), socialMediaLink);
        TemporaryToast('Syccess', 'Small', 'Bottom', 'Saved', 5);
      }
    })
  })
  // Display Social Media Links. -----------------------------------------------
  if ($('.User-Links').length > 0) {
    $.getJSON('get_social_media_accounts/', function(data) {
      for (accountType in data) {
        if (data[accountType].startsWith('https')) {
          addSocialMediaAccount(accountType, data[accountType]);
        }
      }
    })
  }
  // Display Image Reactions Bar. ----------------------------------------------
  $('.Gallery-Modal').hover(
    function() {
      $('.ImageReactions-Bar').css('display', 'flex');
    },
    function() {
      $('.ImageReactions-Bar').css('display', 'none');
    }
  );
  // Edit Profile Informations - Ajax Request. ---------------------------------
  $('.EditProfInfos-btn').click(function() {
    var csrfToken = $('#EditProfInfos-Form').find('input[name=csrfmiddlewaretoken]').val();
    var Data = {
      'address': $('input[name=Address_input]').val(),
      'job': $('input[name=Job_input]').val(),
      'number_phone': $('input[name=NumberPhone_input]').val(),
      'csrfmiddlewaretoken': csrfToken
    };
    $.ajax({
      url: "do_edit/",
      type: "POST",
      data: Data,
      success: function(data) {
        var Message = data.result;
        TemporaryToast('Success', 'Small', 'Bottom', Message, 5);
      }
    });
  });
  // Change Name - Ajax Request. -----------------------------------------------
  $('.ChangeName-btn').click(function() {
    var csrfToken = $('#ChangeName-Form').find('input[name=csrfmiddlewaretoken]').val()
    var Data = {
      'firstName': $('input[name=FirstName_input]').val(),
      'lastName': $('input[name=LastName_input]').val(),
      'csrfmiddlewaretoken': csrfToken
    }
    $.ajax({
      url: "do_change_name/",
      type: "POST",
      data: Data,
      success: function(data) {
        var res = data.result;
        var msg = data.message;
        TemporaryToast(res, 'Small', 'Bottom', msg, 5);
      }
    });
  });
  // Get Social Media Links to Form. -------------------------------------------
  if ($('#EditOtherAccount-Form').length > 0) {
    $.getJSON('get_social_media_accounts/', function(data) {
      var accountType, accountLink, Data;
      accountType = $('.AccountType-select').val().toLowerCase();
      accountLink = data[accountType];
      $('.EditOtherAccount-input').val(accountLink);
      Data = data;
      $('.AccountType-select').change(function(Data) {
        accountType = $('.AccountType-select').val().toLowerCase();
        accountLink = data[accountType];
        $('.EditOtherAccount-input').val(accountLink);
      });
    })
  }
  // Change Social Media Link. -------------------------------------------------
  $('.EditOtherAccount-btn').click(function() {
    var csrfToken = $('#EditOtherAccount-Form').find('input[name=csrfmiddlewaretoken]').val()
    var Data = {
      'Type': $('.AccountType-select').val(),
      'Link': "https://" + $('.EditOtherAccount-input').val(),
      'csrfmiddlewaretoken': csrfToken
    }
    $.ajax({
      url: "do_edit/",
      type: "POST",
      data: Data,
      success: function() {
        TemporaryToast('Success', 'Small', 'Bottom', 'Saved', 5);
      }
    });
  });
  // Remove Social Media Link. ------------------------------------------------
  $('.RemoveOtherAccount-btn').click(function() {
    var csrfToken = $('#EditOtherAccount-Form').find('input[name=csrfmiddlewaretoken]').val()
    var Data = {
      'Type':$('.AccountType-select').val(),
      'csrfmiddlewaretoken': csrfToken
    }
    $.ajax({
      url: "do_remove/",
      type: "POST",
      data: Data,
      success: function() {
        TemporaryToast('Success', 'Small', 'Bottom', 'Saved', 5);
      }
    });
  });
  // Change Email - Ajax Request. ----------------------------------------------
  $('.ChangeEmail-btn').click(function() {
    var currentEmail = $('input[name=Current_Email]').val();
    var newEmail     = $('input[name=New_Email]').val();
    var chkPassword  = $('input[name=Check_Password]').val();
    var csrfToken    = $('#ChangeEmail-Form').find('input[name=csrfmiddlewaretoken]').val();
    var Data = {
      'current_email': currentEmail,
      'new_email': newEmail,
      'check_password': chkPassword,
      'csrfmiddlewaretoken': csrfToken
    };
    $.ajax({
      url: "do_change_email/",
      type: "POST",
      data: Data,
      success: function(data) {
        var res = data.result;
        var msg = data.message;
        TemporaryToast(res, 'Small', 'Bottom', msg, 5);
      }
    });
  });
  // Display/Close Gallery Modal. ----------------------------------------------
  $('img[name^="IMG-"]').click(function() {
    $('.Gallery-Modal').css('display', 'flex');
    $('.Close-GalleryModal').click(function() {
      $('.Gallery-Modal').css('display', 'none');
    })
  });
  // Cahnge Color Active link. -------------------------------------------------

  // Load Profile Gallery. -----------------------------------------------------
  $('.ProfileGallery-Link').click(function() {
    $.getJSON('getgallery/', function(data) {
      console.log(data);
    });
    /* {% for ndx, image in Images_Gallery %}
      <div class="Image-in-Gallery">
        <img name="IMG-{{image.id}}-{{image.Good_Num}}-{{image.Amazing_Num}}-{{image.Stars_Num}}"
             onclick="currentIndex({{ndx}})" src="../../media/{{ image.Image }}">
      </div>
    {% endfor %}
    */
  });
  // Load Profile Papyrus. -----------------------------------------------------
  $('.ProfilePapyrus-Link').click(function() {
    alert('Loaded...');
  });
  // Friendship. ---------------------------------------------------------------
  // Add Friend
  $('.AddFriend-btn').click(function() {
    $('.Friendship-btn').addClass('fa-user-check');
    $('.Friendship-btn').addClass('RemoveFriend-btn');
    $('.Friendship-btn').removeClass('fa-user-plus');
    $('.Friendship-btn').removeClass('AddFriend-btn');
    $('.Friendship-btn').css('color', 'lightblue');
    alert('Added');
  });
  // Cancel Request
  $('.CancelFriend-btn').click(function() {
    true;
  })
  // Remove Friend
  $('.RemoveFriend-btn').click(function() {
    $('.Friendship-btn').addClass('fa-user-plus');
    $('.Friendship-btn').addClass('AddFriend-btn');
    $('.Friendship-btn').removeClass('fa-user-check');
    $('.Friendship-btn').removeClass('RemoveFriend-btn');
    $('.Friendship-btn').css('color', '#c8c8c8');
    alert('Removed');
  })
  // Following. ----------------------------------------------------------------
  $('.Follow-btn').click(function() {
    $('.Following-btn').css('color', 'blue');
  });
  $('UnFollow-btn').click(function() {
    $('.Following-btn').css('color', '#c8c8c8');
  })
  // Add Star. -----------------------------------------------------------------
  $('.AddStar-btn').click(function() {
    $('.AddStar-btn').css('color', 'gold');
  });
  // Checking on Account. ------------------------------------------------------
  if ($('.Profile-Contacts').length > 0) {
    true;
  };
// ------------------------------------------------------------------------------------------------- //
});
// ************************************************************************************************* //
