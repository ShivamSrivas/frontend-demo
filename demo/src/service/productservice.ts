import { Injectable } from '@angular/core';
import {HttpClient } from "@angular/common/http";
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import {Product} from "../domain/product"
    
@Injectable()
export class ProductService {
    private base_url = "http://127.0.0.1:5000"
    constructor (private http:HttpClient) {}

    get_product_details(): Observable<Product[]> {
        return this.http.get<Product[]>(this.base_url + '/get_all_details');
    }

    add_products(product: any) {
        return this.http.post(this.base_url + '/add_product', product);
    }
    
    updateProduct(id: string, product: Product) {
        return this.http.put(this.base_url + `/update_product/${id}`, product);
    }
    deleteProduct(id:string){
        return this.http.delete(this.base_url + `/delete_product/${id}`)
    }

    getProductsMini(): Observable<Product[]> {
        return this.get_product_details().pipe(
            map((products: Product[]) => products)
        );
    }


};