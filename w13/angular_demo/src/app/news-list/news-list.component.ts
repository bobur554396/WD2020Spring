import {Component, OnInit} from '@angular/core';
import {CategoryService} from "../category.service";
import {Category} from "../models";

@Component({
  selector: 'app-news-list',
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.css']
})
export class NewsListComponent implements OnInit {
  categories: Category[] = [];

  constructor(public categoryService: CategoryService) {
  }

  ngOnInit(): void {
    this.getCategoryList();
  }

  getCategoryList() {
    this.categoryService.getCategoryList()
      .subscribe(categories => {
        this.categories = categories
      });
  }

  deleteCategory(id) {
    this.categoryService.deleteCategory(id).subscribe(res => {
      // this.categories = this.categories.filter(c => c.id != id);
      // this.getCategoryList();
    });
  }

}
