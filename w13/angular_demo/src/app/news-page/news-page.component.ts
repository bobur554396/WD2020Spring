import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {CategoryService} from "../category.service";
import {Category} from "../models";

@Component({
  selector: 'app-news-page',
  templateUrl: './news-page.component.html',
  styleUrls: ['./news-page.component.css']
})
export class NewsPageComponent implements OnInit {
  category: Category;

  constructor(private categoryService: CategoryService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCategory();
  }

  getCategory() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.categoryService.getCategory(id).subscribe(category => this.category = category);
  }

}
