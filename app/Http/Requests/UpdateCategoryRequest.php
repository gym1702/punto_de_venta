<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class UpdateCategoryRequest extends FormRequest
{
    public function authorize()
    {
        return true;
    }

    
    public function rules()
    {
        return [
            'nombre'=>'required|string|unique:categories,nombre,'. 
            $this->route('category')->id.'|max:100',

            'descripcion'=>'nullable|string|max:250',
        ];
    }


    public function messages()
    {
        return [
            'nombre.required'=>'Este campo es requerido',
            'nombre.string'=>'El valor no es correcto',
            'nombre.max'=>'Solo se permiten 50 caracteres',
            'nombre.unique'=>'La categoria ya existe',
            
            'descripcion.string'=>'El valor no es correcto',
            'descripcion.max'=>'Solo se permiten 250 caracteres',
        ];
    }
}
