
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
}
function updateCatalogTask() {
  var frm = $('.contact-form');
  task_id = myStorage.getItem('task_catalog_id');
  var serTaskId ='';
  if(task_id) {
    var serTaskId = '&task_id=' + task_id
  }
  serFrm = frm.serialize() + serTaskId;
  console.log('serFrm', serFrm);
  $.ajax({
    type: "POST",
    url: '/tasks/update-contact-form',
    data: serFrm,
    success: (json)=> {
      console.log(json);
      myStorage.setItem('task_catalog_id',json.task_id );
      getUserTasks();
    },
    dataType: "json"
  });
}


function updateLikedProductsTask() {
  var frm = $('#likedProductsForm');
  task_id = myStorage.getItem('task_products_id');
  var serTaskId ='';
  if(task_id) {
    var serTaskId = '&task_id=' + task_id
  }
  serFrm = frm.serialize() + serTaskId;
  console.log('serFrm', serFrm);
  $.ajax({
    type: "POST",
    url: '/tasks/update-products-form',
    data: serFrm,
    success: (json)=> {
      debugger;
      console.log(json);
      myStorage.setItem('task_products_id',json.task_name );
      getUserTasks();
      for(var i = 0; i< json.products_list.length; i++) {
        img = json.products_list[i];
        var slick_slide = $(`[data-prod-id="${img.id}"`);
        slick_slide.data('is-added',true);
      }
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
function addClientLikeProduct(prodId) {
  //products = $('#likedProductsForm > products[]');
  $('#likedProductsForm').append(`<input type="text" name="products[]" value="${prodId}"id="">`);
  $('#likedProductsForm').trigger('change');
  $('#modal-add-btn').prop('disabled', true);
  $('#modal-add-btn').text('נוסף להצעת מחיר');
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
          <li><img src=${product.image_thumbnail} height="50px"/> <span>${product.title}</span>
        `
      }
      productsMarkup += '</ul>';
      $('#cartProductsList').html(productsMarkup);
    },
    dataType: "json"
  });
}

function loadProductsModal() {
  $('#likedProductsModal').modal('show');
  $('#likedProductsModal .close-modal').click(function () {
    $('#likedProductsModal').modal('hide');
  });
  updateProductsCart();
}

function openCategoryModal(albumId) {
  debugger;
  var albums = getAllAlbums();
  var album = albums.find((val, idx, obj) => {
    return val.id == albumId
  });
  var imagesMarkup = '<div class="category-items">'
  for(var i = 0; i < album.images_list.length;i++) {
    img = album.images_list[i];
    imagesMarkup+= `<div class="category-item" onclick="$('.my-slick-slide[data-prod-id=${img.id}]').click();" data-category-prod-id="${img.id}">
                    <img width="250px" height="250px" src="${img.image_thumbnail}" alt="${img.description}" />
                    <div class="img-title">${img.title}</div>
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