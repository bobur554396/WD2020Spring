import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { NEWS_LIST } from './newsList';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  news = NEWS_LIST;

  addNews() {
    this.news.push({
      id: Math.max(...NEWS_LIST.map(item => item.id)) + 1,
      title: 'New News',
      description: 'OMG NEWS'
    });
  }

  removeNewsPageById(id) {
    this.news = this.news.filter(newsPage => newsPage.id !== id)
  }

  changeNewsPageTitleById(id, newTitle) {
    this.news.find(newsPage => newsPage.id === id).title = newTitle;
  }

  getNewsList(): Observable<string[]> {
    return of(this.news);
  }

  getNewsPageById(id): Observable<any> {
    const neededNewsPage = this.news.find(newsPage => newsPage.id === id);
    return of(neededNewsPage);
  }

}
