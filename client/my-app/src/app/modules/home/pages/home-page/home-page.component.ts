import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  constructor(private userService: UserService) {}

  ngOnInit(): void {}

  public triggerGetUser() {
    this.getUser();
  }

  public triggerGetUsers() {
    this.getUserList();
  }

  private getUser() {
    this.userService
      .getUser(1)
      .subscribe({ next: user => console.log('user', user) });
  }

  private getUserList() {
    this.userService
      .listUsers()
      .subscribe({ next: users => console.log('users', users) });
  }
}
