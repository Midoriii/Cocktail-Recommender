import { Component, OnInit, Input } from '@angular/core';
import { Drink } from 'src/app/models/drink.model';

@Component({
  selector: 'app-drink',
  templateUrl: './drink.component.html',
  styleUrls: ['./drink.component.scss']
})
export class DrinkComponent implements OnInit {
  @Input() drink: Drink;

  constructor() { }

  ngOnInit() {}

}
