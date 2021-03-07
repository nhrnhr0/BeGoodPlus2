
$(document).on('show.bs.modal', '.modal', function (event) {
  var zIndex = 1040 + (10 * $('.modal:visible').length);
  $(this).css('z-index', zIndex);
  setTimeout(function() {
      $('.modal-backdrop').not('.modal-stack').css('z-index', zIndex - 1).addClass('modal-stack');
  }, 0);
});
$(document).on('hidden.bs.modal', '.modal', function () {
  $('.modal:visible').length && $(document.body).addClass('modal-open');
});

function setCatalogTaskListiner() {
  var frm = $('.contact-form');
  frm.change(function(){
    console.log('update Catalog Task');
    updateCatalogTask();
  });

  var productsFrm = $('#likedProductsForm');
  productsFrm.change(function() {
    console.log('update Products Task');
    updateLikedProductsTask();
  });

  setFormAutoSave(productsFrm)
}
function updateCatalogTask(isSubmited=false) {
  debugger;
  var frm = $('.contact-form');
  task_id = myStorage.getItem('task_catalog_id');
  var serTaskId ='';
  if(task_id) {
    var serTaskId = `&task_id=${task_id}&submited=${isSubmited}`
  }
  serFrm = frm.serialize() + serTaskId;
  
  if(isSubmited) {
    isValid = frm.get(0).reportValidity();
    if(isValid == false) {
      alert('שם פאלפון ואימייל הם שדות חובה');
      return;
    }
  }

  $.ajax({
    type: "POST",
    url: '/tasks/update-contact-form',
    data: serFrm,
    success: (json)=> {
      console.log(json);
      myStorage.setItem('task_catalog_id',json.task_id );
      if (json.task_id == -1) {
        frm.trigger("reset");
        resetContactFormAutoSave();
      }
      getUserTasks();
      updateProductsCart();
    },
    dataType: "json"
  });
}
function submitCatalogContactForm() {
  debugger;
  updateCatalogTask(isSubmited=true);
  

}
function submitCatalogProducts() {
  updateLikedProductsTask(isSubmited=true);
  window.location.href = window.location.href;

}
// TODO: send the ajax once and not once per input field
function updateLikedProductsTask(isSubmited=false) {
  var frm = $('#likedProductsForm');
  task_id = myStorage.getItem('task_products_id');
  var serTaskId ='';
  if(task_id) {
    //var serTaskId = '&task_id=' + task_id
    var serTaskId = `&task_id=${task_id}&submited=${isSubmited}`;
  }
  serFrm = frm.serialize() + serTaskId;
  if(isSubmited) {
    isValid = frm.get(0).reportValidity();
    if(isValid == false) {
      alert('שם פאלפון ואימייל הם שדות חובה');
      return;
    }
  }
  $.ajax({
    type: "POST",
    url: '/tasks/update-products-form',
    data: serFrm,
    success: (json)=> {
      console.log(json);
      //myStorage.setItem('task_products_name',json.task_name );
      myStorage.setItem('task_products_id',json.task_id );
      if (json.task_id == -1) {
        frm.trigger("reset");
        resetFormAutoSave(frm);
        $('#cartProductsList').empty();
        getUserTasks();
      }

      /*getUserTasks();
      for(var i = 0; i< json.products_list.length; i++) {
        img = json.products_list[i];
        var slick_slide = $(`[data-prod-id="${img.id}"`);
        slick_slide.data('is-added',true);
        updateClientLikedUI1(img.id);
      }*/
    },
    dataType: "json"
  });
}





// handle client liked images:
/*
function getClientLinkedProducts() {
  var products = myStorage.getItem('client_liked_products');
  if (products == undefined) {
    return undefined;
  } else {
    return JSON.parse(products);
  }
}

function setClientLinkedProducts(products) {
  myStorage.setItem('client_liked_products', JSON.stringify(products));
}
*/
function modal_add_btn_click() {
  
}
function updateClientLikedUI() {
  console.log('hey');
  liked_products = $('#likedProductsForm input[name="products[]"]');
  for(var i = 0; i<liked_products.length;i++) {
    updateClientLikedUI1(liked_products.val());
  }

}
function updateClientLikedUI1(prodId) {
  $(`.my-slick-slide[data-prod-id=${prodId}]`).addClass('checked');
  $(`.category-item[data-category-prod-id="${prodId}"]`).addClass('checked');
}
function removeClientLikedUI1(prodId) {
  $(`.my-slick-slide[data-prod-id=${prodId}]`).removeClass('checked');
  $(`.category-item[data-category-prod-id="${prodId}"]`).removeClass('checked');
}

// delete the product from the user form
function removeClientLikeProduct(prodId) {
  var productsToRemove = $(`#likedProductsForm :input[name="products[]"]`).filter(function() {
    return this.value == prodId
  });
  debugger;
  productsToRemove.remove();
  removeClientLikedUI1(prodId);
  var cartId = myStorage.getItem('task_products_id');
  var serTaskId ='';
  if(cartId) {
    var serTaskId = `&cartId=${cartId}&prodId=${prodId}`
  }
  serFrm = frm.serialize() + serTaskId;
  
  $.ajax({
    type: "POST",
    url: `tasks/delete-user-liked-product/`,
    data: serFrm,
    success: (json)=> {
      console.log('product deleted in the server', json);
    }
  });
  $('#deleteProductForm')
  
  updateLikedProductsTask();
}
function addClientLikeProduct(prodId) {
  //products = $('#likedProductsForm > products[]');
  $('#likedProductsForm').append(`<input type="text" name="products[]" value="${prodId}"id="">`);
  $('#likedProductsForm').trigger('change');
  $('#modal-add-btn').prop('disabled', true);
  $('#modal-add-btn').text('נוסף להצעת מחיר');
  $('#modal-add-btn').addClass('isAdded');
  updateClientLikedUI1(prodId);
  getUserTasks();

  // bell animation:
  $('#navbarDropdown').removeClass('notify');
  $('#navbarDropdown').offsetWidth = $('#navbarDropdown').offsetWidth;
  setTimeout(()=>{
    $('#navbarDropdown').addClass('notify');
  },200);
  setTimeout(updateProductsCart, 500);
  console.log('addClientLikeProduct done');
  /*
  products = getClientLinkedProducts();
  var found = false;
  if (products == undefined) {
    products = [];
  }
  for (var i = 0; i < products.length; i++) {
    if (products[i] == prodId) {
      found = true;
    }
  }
  if (found == false) {
    products.push(prodId);
    setClientLinkedProducts(products);
    updateLikedProductsTask();
  }*/
}

function updateProductsCart() {
  $.ajax({
    type: "GET",
    url: '/tasks/get-user-cart',
    //data: serFrm,
    success: (json)=> {
      console.log(json);
      //myStorage.setItem('task_catalog_id',json.task_id );
      //getUserTasks();
      var productsMarkup = '<ul>';
      for(var i = 0; i < json.products_list.length; i++) {
        
        product = json.products_list[i];
        productsMarkup += `
          <li data-prod-id="${product.id}">
            <div>
              <img src=${product.image_thumbnail} height="50px"/>
              <span>${product.title}</span>
            </div>
            <div>
              <button type='button' data-prod-id="${product.id}" onclick="deleteLikedProductBtn(${product.id});" ><span >&times;</span></button>
            </div>
          </li>
        `
        updateClientLikedUI1(product.id);
      }
      productsMarkup += '</ul>';
      $('#cartProductsList').html(productsMarkup);
    },
    dataType: "json"
  });
}

// delete the product from the user cart in the html and in the form
function deleteLikedProductBtn(prodId) {
  console.log('delete me');
  $(`li[data-prod-id="${prodId}"`).remove();
  removeClientLikeProduct(prodId);
}

function loadProductsModal() {
  $('#likedProductsModal').modal('show');
  $('#likedProductsModal .close-modal').click(function () {
    $('#likedProductsModal').modal('hide');
  });
  updateProductsCart();
}

function openCategoryModal(albumId) {
  //updateLikedProductsTask();
  updateProductsCart();
  var albums = getAllAlbums();
  var album = albums.find((val, idx, obj) => {
    return val.id == albumId
  });
  var imagesMarkup = '<div class="category-items">'
  for(var i = 0; i < album.images_list.length;i++) {
    img = album.images_list[i];
    imagesMarkup+= `<div class="category-item" data-category-prod-id="${img.id}">
                    <img width="250px" height="250px" onclick="$('.my-slick-slide[data-prod-id=${img.id}]').click();" src="${img.image_thumbnail}" alt="${img.description}" />
                    <div class="img-title">${img.title}</div>
                    <div onclick="$('.my-slick-slide[data-prod-id=${img.id}] [name=like-btn]').click();" class="like-btn" name="like-btn">
                      <i name="like-btn" class="fa fa-heart"></i>
                    </div>
                    </div>
      `
  }
  imagesMarkup += '</div>'
  $('#categoryModal .modal-title').text(album.title);
  $('#categoryModal .modal-body').html(imagesMarkup);
  $('#categoryModal').modal('show');
  $('#categoryModal .close-modal').click(function () {
    $('#categoryModal').modal('hide');
  });
}

setCatalogTaskListiner();
getUserTasks();