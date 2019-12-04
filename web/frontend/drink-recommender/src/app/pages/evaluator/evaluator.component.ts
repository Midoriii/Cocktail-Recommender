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
  recommendedDrinksNumber = 1;
  baseDrinks: Drink[] = [];
  recommendedDrinks: Drink[][];

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.initializeEvaluator();
  }

  initializeEvaluator() {
    const baseDrinkIndices = [];
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
        this.recommendedDrinks = drinks;
      },
      error => console.log('An error occured during fetching recommendations.', error)
    );
  }

  rateRecommender(id: number) {
    this.initializeEvaluator();
    this.api.rateRecommender(id).subscribe(
      (status: string) => {
        console.log('New status is ', status);
      },
      error => {
        console.log('An error occured during sending rating.', error);
      }
    );
  }

}
