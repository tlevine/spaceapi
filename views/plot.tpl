<html>
  <head>
    <style>
    .observation a { width: 100%; height: 100%; display: block; }
    .observation { background-color: blue; }
    </style>
  </head>
  <body>
    <table id="plot">
      <thead>
        <tr>
          <th>Date</th>
          <th colspan="72">
        </tr>
      </thead>
      <tbody>
        % for week in weeks
          <tr>
            <td class="date">{{week['date']}}</td>
            % for observation in week['observations']
            <td class="observation"><a href="{{observation['mirror_href']}}"></a></td>
          </tr>
      </tbody>
    </table>
  </body>
</html>
