import { Component, OnInit , Input} from '@angular/core';
import { Wishlist } from '../Wishlist';

@Component({
  selector: 'app-wishlist-item',
  templateUrl: './wishlist-item.component.html',
  styleUrls: ['./wishlist-item.component.css']
})
export class WishlistItemComponent implements OnInit {
  @Input() wishlist: Wishlist;
  constructor() { }

  ngOnInit(): void {
  }

}
