import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { SearchItem } from '../SearchItem';
import { SearchService } from '../services/search.service';  

@Component({
  selector: 'app-search-item',
  templateUrl: './search-item.component.html',
  styleUrls: ['./search-item.component.css']
})
export class SearchItemComponent implements OnInit {
  // @Input() searchItems: SearchItem;
 searchItems: SearchItem[] = [];
 // @Input() searchItems: SearchItem[];
  constructor(private searchService: SearchService, private _router:Router) { }

  ngOnInit(): void {
    if (this.searchService.subsVar==undefined) {    
      this.searchService.subsVar = this.searchService.   
      invokeSearchCallFunction.subscribe((searchQuery:string) => {    
        this.submitSearch(searchQuery); 
      }); 
    }
  }

  submitSearch(searchQuery:String){
   // console.log('Came here!!!' + searchQuery.value.search);
    this.searchService.getSearchItems(searchQuery).subscribe((searchItems) =>{
      this.searchItems = searchItems;    
            
    }  );
  }

  onSubmitSearchFunction(searchQuery){
    this.searchService.onSubmitSearch(searchQuery);
  }

}
