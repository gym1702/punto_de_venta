<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    protected $fillable = [
        'nombre',
        'descripcion',
    ];

    // RELACIONA A PRODUCTOS CON CATEGORIAS
//     public function productos()
//     {
//         return $this->hasMany(Product::class);
//     }
}
