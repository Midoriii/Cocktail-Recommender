import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Drink } from 'src/app/models/drink.model';

@Component({
  selector: 'app-drink',
  templateUrl: './drink.component.html',
  styleUrls: ['./drink.component.scss']
})
export class DrinkComponent implements OnInit {
  @Input() drink: Drink;
  @Input() hideDetails: boolean;
  @Input() showLike: boolean;
  @Output() likedDrink = new EventEmitter();
  icon = 'favorite_border';
  liked = false;

  constructor() { }

  ngOnInit() {}

  onLikeDrink() {
    if (this.liked) {
      this.likedDrink.emit({"drink": this.drink, "liked": false});
      this.icon = 'favorite_border';
      this.liked = false;
    } else {
      this.likedDrink.emit({"drink": this.drink, "liked": true});
      this.icon = 'favorite';
      this.liked = true;
    }
  }

}
