<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Http\Requests\StoreCategoryRequest;
use App\Http\Requests\UpdateCategoryRequest;

class CategoryController extends Controller
{
    public function index()
    {
        $categories = Category::all();
        return view('admin.categorias.index', compact('categories'));
    }

    
    public function create()
    {
        return view('admin.categorias.create');
    }

   
    public function store(StoreCategoryRequest $request)
    {
        Category::create($request->all());
        return redirect()->route('categories.index')->with('registrado', 'Si');
    }

   
    public function show(Category $category)
    {
        return view('admin.categorias.show', compact('category'));
    }

   
    public function edit(Category $category)
    {
        return view('admin.categorias.edit', compact('category'));
    }

    
    public function update(UpdateCategoryRequest $request, Category $category)
    {
        $category->update($request->all());
        return redirect()->route('categories.index')->with('actualizado', 'Si');
    }

    
    public function destroy(Category $category)
    {
        $category->delete();
        return redirect()->route('categories.index');
    }
}
