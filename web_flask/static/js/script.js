// $(document).ready(init);
// const host = 'localhost';
// const port = '5001'

// function init() {
//     const url = `${host}:${port}/api/v1/products`
//     $.get(url, (data, status) => {
//         if (data.status === 'OK') {
//             data.forEach((product) => {
//                 $('div#product-row').append(
//                     `<div class="col-lg-4 col-md-6 col-sm-6 pb-1">
//                     <div class="product-item bg-light mb-4">
//                         <div class="product-img position-relative overflow-hidden">
//                             <img class="img-fluid w-100" src="../static/img/${product.image_name}" alt="">
//                             <div class="product-action">
//                                 <a class="btn btn-outline-dark btn-square" href=""><i class="fa fa-shopping-cart"></i></a>
//                                 <a class="btn btn-outline-dark btn-square" href=""><i class="far fa-heart"></i></a>
//                                 <a class="btn btn-outline-dark btn-square" href=""><i class="fa fa-sync-alt"></i></a>
//                                 <a class="btn btn-outline-dark btn-square" href=""><i class="fa fa-search"></i></a>
//                             </div>
//                         </div>
//                         <div class="text-center py-4">
//                             <a class="h6 text-decoration-none text-truncate" href="">${product.name}</a>
//                             <div class="d-flex align-items-center justify-content-center mt-2">
//                                 <h5>${product.price}</h5><h6 class="text-muted ml-2"></h6>
//                             </div>
//                             <div class="d-flex align-items-center justify-content-center mb-1">
//                                 <small class="fa fa-star text-primary mr-1"></small>
//                                 <small class="fa fa-star text-primary mr-1"></small>
//                                 <small class="fa fa-star text-primary mr-1"></small>
//                                 <small class="fa fa-star text-primary mr-1"></small>
//                                 <small class="fa fa-star text-primary mr-1"></small>
//                                 <small>(${product.reviews.length})</small>
//                             </div>
//                         </div>
//                     </div>
//                 </div>`
//                 )
//             });
//         }
//     });
// }