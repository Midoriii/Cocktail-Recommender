import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Drink } from '../models/drink.model';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  public getDrink(id: number): Observable<Drink> {
    return this.http.get<Drink>(environment.apiUrl + `/drink/${id}`).pipe(map((d: Drink) => { d.Id = id; return d;}));
  }

  public getRecommendedDrinks(baseDrinksIndices: number[], c: number): Observable<Drink[][]> {
    return this.http.post<Drink[][]>(environment.apiUrl + '/recommend', {indices: baseDrinksIndices, count: c});
  }
}
