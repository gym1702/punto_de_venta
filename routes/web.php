<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\CategoryController;


// Route::get('/', function () {
//     return view('layouts.admin');
// });


//Cerar esta rura pra redireccionar a login
Route::get('/', function () {
    return view('layouts.ingresar');
});


//Inicio
//Modificar tambien en Home contoller hacia a donde apunta el index
Route::get('home',[HomeController::class, 'index']);

Route::resource('categories', CategoryController::class);
Route::get('Eliminar-Categoria/{category}',[CategoryController::class, 'destroy']);


Auth::routes();
