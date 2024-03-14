document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    stars.forEach(function(star) {
      star.addEventListener('mouseover', starOver);
      star.addEventListener('click', starClick);
    });
  
    function starOver(e) {
      const value = +e.target.dataset.value;
      stars.forEach(function(star) {
        if (+star.dataset.value <= value) {
          star.textContent = '★'; 
        } else {
          star.textContent = '☆'; 
        }
      });
    }
  
    function starClick(e) {
      const value = +e.target.dataset.value;
      console.log(`Rated: ${value} stars`);
    }
  });



 
  // Get all the reply buttons
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // Get the ID of the reply form to be displayed
      const replyFormId = this.getAttribute('data-comment-id');
      // Display the corresponding reply form
      document.getElementById(replyFormId).style.display = 'block';
    });
  });

  // Get all the submit reply buttons
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // Add logic here to submit a reply, like using AJAX to send a reply to the server
      alert('Reply submitted');
      // Hide the reply form
      this.parentElement.style.display = 'none';
    });
  });

function copyLink() {
    var copyText = document.getElementById("shareLinkInput");
    copyText.select(); // select text
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value); // copy the text to clipboard

    navigator.clipboard.writeText(copyText.value).then(() => {
      // show Toast after copied
      var toastEl = document.getElementById('copyToast');
      var toast = new bootstrap.Toast(toastEl);
      toast.show();
      var shareModalEl = document.getElementById('shareModal');
      var shareModal = bootstrap.Modal.getInstance(shareModalEl);
      shareModal.hide();
    }, () => {
      // fail to copy
      // I don't think we need this
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    const paginationLinks = document.querySelectorAll('.pagination .page-link');

    paginationLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // prevent default
            event.preventDefault();

            // remove active
            document.querySelector('.pagination .active').classList.remove('active');

            // change to active
            const parentListItem = this.parentNode;
            if (parentListItem.tagName === 'LI') {
                parentListItem.classList.add('active');
                // update aria-current if needed
                if (this.tagName === 'A') {
                    this.parentNode.innerHTML = `<span class="page-link">${this.textContent}</span>`;
                }
            }


            // can use AJAX to load page contect
        });
    });
});

function checkPasswordsInRegistration() {
  var password = document.getElementById('id_password1').value;
  var confirmPassword = document.getElementById('id_password2').value;
  var message = document.getElementById('checkPasswordRegistration');

  if (password === confirmPassword) {
    message.style.color = 'green';
    message.textContent = "Passwords match.";
    // logic for matched password
  } else {
    message.style.color = 'red';
    message.textContent = "Passwords do not match.";
    confirmPassword.style.borderColor = 'red';
    // logic for not matched password
  }
}

function checkPasswords() {
  var password = document.getElementById('change-password').value;
  var confirmPassword = document.getElementById('change-password-confirm').value;
  var message = document.getElementById('checkPassword');

  if (password === confirmPassword) {
    message.style.color = 'green';
    message.textContent = "Passwords match.";
    // logic for matched password
  } else {
    message.style.color = 'red';
    message.textContent = "Passwords do not match.";
    confirmPassword.style.borderColor = 'red';
    // logic for not matched password
  }
}

document.getElementById('ColorInput').addEventListener('input', changeBackgroundColor);

function changeBackgroundColor() {
  var color = document.getElementById('ColorInput').value;
  document.body.style.backgroundColor = color;
};

  