import { Component, OnInit } from '@angular/core';
import { ImportsModule } from './imports';
import { Product } from '@domain/product';
import { firstValueFrom } from 'rxjs';
import { ProductService } from '@service/productservice';

@Component({
  selector: 'table-template-demo',
  templateUrl: 'table.component.html',
  standalone: true,
  imports: [ImportsModule],
  providers: [ProductService]
})
export class TableTemplateDemo implements OnInit {
  products: Product[] = [];
  visible: boolean = false;
  mode: string = 'add';
  add_products: Product = {
    id: '', 
    name: '',
    code: '',
    description: '',
    image: '',
    price: 0,
    category: '',
    quantity: 0,
    inventoryStatus: '',
    rating: 0 
  };

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.refreshProducts();
  }

  resetProduct() {
    this.add_products = {
      id: '', 
      name: '',
      code: '',
      description: '',
      image: '',
      price: 0,
      category: '',
      quantity: 0,
      inventoryStatus: '',
      rating: 0
    };
  }
  getSeverity(status: string) {
    switch (status) {
      case 'INSTOCK':
        return 'success';
      case 'LOWSTOCK':
        return 'warning';
      case 'OUTOFSTOCK':
        return 'danger';
      default:
        return 'success';
    }
  }

  showDialog(value: boolean, mode: string) {
    this.visible = value;
    this.mode = mode;
    if (mode === 'add') {
      this.resetProduct();
    }
  }

  async refreshProducts() {
    try {
      const data = await firstValueFrom(this.productService.getProductsMini());
      this.products = data;
      console.log("Products successfully fetched:", this.products);
    } catch (error) {
      console.error('Error fetching products:', error);
      this.handleError("Failed to fetch products. Please try again.");
    }
  }

  async addData() {
    if (this.mode === 'add') {
      try {
        const response = await firstValueFrom(this.productService.add_products(this.add_products));
        console.log("Product added successfully:", response);
        this.showDialog(false, 'add');
        this.refreshProducts();
      } catch (error) {
        console.error("Error adding product:", error);
        this.handleError("Failed to add product. Please try again.");
      }
    } else if (this.mode === 'edit' && this.add_products.id) {
      try {
        const response = await firstValueFrom(this.productService.updateProduct(this.add_products.id, this.add_products));
        console.log("Product updated successfully:", response);
        this.showDialog(false, 'edit');
        this.refreshProducts();
      } catch (error) {
        console.error("Error updating product:", error);
        this.handleError("Failed to update product. Please try again.");
      }
    }
  }

  editData(product: Product) {
    this.add_products = { ...product };
    this.showDialog(true, 'edit');
  }

  async deleteData(id: string) {
    try {
      const response = await firstValueFrom(this.productService.deleteProduct(id));
      console.log("Product deleted successfully:", response);
      this.refreshProducts();
    } catch (error) {
      console.error("Error in product deletion:", error);
      this.handleError("Failed to delete product. Please try again.");
    }
  }

  private handleError(message: string) {
    alert(message);
  }
}
