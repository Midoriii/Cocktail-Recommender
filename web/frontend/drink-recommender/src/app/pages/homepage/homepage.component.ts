import { Component, OnInit } from '@angular/core';
import { Drink } from 'src/app/models/drink.model';
import { ApiService } from 'src/app/services/api.service';
import { Subscription, Observable, forkJoin } from 'rxjs';
import { initialDrinks } from './initial-drinks';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  initialDrinks = initialDrinks;

  initialDrinksSaved: Drink[][] = [];

  likedDrinks: number[] = [];

  selectedIndex = 0;

  showRecommendationsPanel = false;
  recommendedDrinks: Drink[] = [];

  loading = false;

  constructor(private api: ApiService) { }

  ngOnInit() {
    
  }

  addLikedDrink(event: any) {
    if (event.liked) {
      this.likedDrinks.push(event.drink.Id);
    } else {
      this.likedDrinks = this.likedDrinks.filter(obj => obj !== event.drink.Id);
    }
    console.log("liked drinks", this.likedDrinks);
  }

  showRecommendedDrinks() {
    this.loading = true;
    this.api.getRecommendedDrinks(this.likedDrinks, 20).subscribe(
      (drinks: Drink[][]) => {
        this.recommendedDrinks = drinks[2];
        this.loading = false;
        this.showRecommendationsPanel = true;
      },
      err => {
        this.loading = false;
      }
    );
  }

}

