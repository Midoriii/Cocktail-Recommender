import { Component, OnInit } from '@angular/core';
import { Drink } from 'src/app/models/drink.model';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-evaluator',
  templateUrl: './evaluator.component.html',
  styleUrls: ['./evaluator.component.scss']
})
export class EvaluatorComponent implements OnInit {
  baseDrinksNumber = 1;
  recommendedDrinksNumber = 3;
  baseDrinks: Drink[] = [];
  recommendedDrinks1: Drink[] = [];
  recommendedDrinks2: Drink[] = [];
  recommendedDrinks3: Drink[] = [];

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.initializeEvaluator();
  }

  initializeEvaluator() {
    const baseDrinkIndices = [];
    this.recommendedDrinks1 = [];
    this.recommendedDrinks2 = [];
    this.recommendedDrinks3 = [];
    this.baseDrinks = [];

    for (let i = 0; i < this.baseDrinksNumber; i++) {
      const randomDrinkId = Math.floor(Math.random() * 2000);
      baseDrinkIndices.push(randomDrinkId);
      this.api.getDrink(randomDrinkId).subscribe(
        (drink: Drink) => {
          this.baseDrinks.push(drink);
        },
        error => console.log(`An error occured during fetching drink ${randomDrinkId}`, error)
      );
    }

    this.api.getRecommendedDrinks(baseDrinkIndices, 3).subscribe(
      (drinks: Drink[][]) => {
        this.recommendedDrinks1 = drinks[0];
        this.recommendedDrinks2 = drinks[1];
        this.recommendedDrinks3 = drinks[2];
      },
      error => console.log('An error occured during fetching recommendations.', error)
    );
  }

}
