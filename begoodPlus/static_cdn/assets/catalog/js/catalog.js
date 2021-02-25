//setContactFormAutoSave();

/*function setContactFormAutoSave() {
  var taskName = 'catalog';
  set_autosave(document.querySelector('.contact-form #id_name'), taskName + '_name')
  set_autosave(document.querySelector('.contact-form #id_phone'), taskName + '_phone')
  set_autosave(document.querySelector('.contact-form #id_email'), taskName + '_email')
  set_autosave(document.querySelector('.contact-form #id_message'), taskName + '_message')
}*/

/*
function setCatalogTaskListiner() {
  document.querySelector('.contact-form #id_name').addEventListener('change', function () {
    checkCatalogFormTask();
  });
  document.querySelector('.contact-form #id_phone').addEventListener('change', function () {
    checkCatalogFormTask();
  });
  document.querySelector('.contact-form #id_email').addEventListener('change', function () {
    checkCatalogFormTask();
  });

  document.querySelector('.contact-form #id_message').addEventListener('change', function () {
    checkCatalogFormTask();
  });
}

function checkCatalogProductsTask() {
  var products = getClientLinkedProducts();
  if (products == undefined || products == "") {
    deleteClientTask('catalog_images');
  } else {
    setClientTask('catalog_images', {
      'msg': 'לא שלחת את המוצרים שאהבת',
      'url': '/testCatalog#sendProductsModal',
      //'onclick':`$('#catalogProductsModal').modal('show');`,
      'onclick':`$('#catalogProductsModal').modal('show');`
    });
  }
}

function checkCatalogFormTask() {
  if (document.querySelector('.contact-form #id_name').value != "" ||
    document.querySelector('.contact-form #id_phone').value != "" ||
    document.querySelector('.contact-form #id_email').value != "" ||
    document.querySelector('.contact-form #id_message').value != "") {
    setClientTask('catalog', {
      'msg': 'לא סיימת למלא טופס יצירת קשר בקטלוג',
      'url': '/testCatalog#contact-form'
    });
  } else {
    deleteClientTask('catalog');
  }
}


function getClientLinkedProducts() {
  var products = myStorage.getItem('client_liked_products');
  if (products == undefined) {
    return undefined;
  } else {
    return JSON.parse(products);
  }
}

function setClientLinkedProducts(products) {
  myStorage.setItem('client_liked_products', JSON.stringify(products)); +
  checkCatalogProductsTask();
}

function addClientLikeProduct(prodId) {
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
    setClientLinkedProducts(products)
  }
}

function refreshCatalogProductsModal() {
  debugger;
  var liked = getClientLinkedProducts();
  var albums = getAllAlbums();

  var modalBodyMarkup = `
    <table>
      <thead>
        <tr>מוצר</tr>
        <tr>שם</tr>
      </thead>
      <tbody>
   
   `;
  for (var i = 0; i < liked.length; i++) {
    product = findProductFromAlbum(albums, liked[i]);
    modalBodyMarkup += `<tr>
      <td>${product.image}</td>
      <td>${product.title}</td>
    </tr>`
  }
  modalBodyMarkup += `
  </tbody>
</table>
`
}

function findProductFromAlbum(albums, prodId) {
  for (var i = 0; i < albums.length; i++) {
    for (var j = 0; j < albums[i].images_list.length; j++) {
      if (albums[i].images_list[j].id == prodId) {
        return albums[i].images_list[j];
      }
    }
  }

}



//TODO: this is not fucking working!
if (window.location.hash == '#sendProductsModal') {
    refreshCatalogProductsModal();
    $('#catalogProductsModal').modal('show');

}
setCatalogTaskListiner();
*/

function setMainTaskListiner() {
  var frm = $('.contact-form');
  frm.change(function(){
    console.log('update Catalog Task');
    updateCatalogTask();
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
      myStorage.setItem('task_catalog_id',json.task_id )
    },
    dataType: "json"
  });
}


setMainTaskListiner();