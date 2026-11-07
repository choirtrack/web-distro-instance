<?php declare(strict_types = 1);

namespace Drupal\robtestblock\Plugin\Block;

use Drupal\Core\Access\AccessResult;
use Drupal\Core\Block\BlockBase;
use Drupal\Core\Form\FormStateInterface;
use Drupal\Core\Session\AccountInterface;
use Drupal\views\Views;

/**
 * Provides a rob test block block.
 *
 * @Block(
 *   id = "robtestblock_rob_test_block",
 *   admin_label = @Translation("rob test block"),
 *   category = @Translation("Custom"),
 * )
 */
final class RobTestBlockBlock extends BlockBase {

  /**
   * {@inheritdoc}
   */
  public function defaultConfiguration(): array {
    return [
      'example' => $this->t('Hello world!'),
    ];
  }

  /**
   * {@inheritdoc}
   */
  public function blockForm($form, FormStateInterface $form_state): array {
    $form['example'] = [
      '#type' => 'textarea',
      '#title' => $this->t('Example'),
      '#default_value' => $this->configuration['example'],
    ];
    return $form;
  }

  /**
   * {@inheritdoc}
   */
  public function blockSubmit($form, FormStateInterface $form_state): void {
    $this->configuration['example'] = $form_state->getValue('example');
  }

  /**
   * {@inheritdoc}
   */
  public function build(): array {


/*
// Get current route object.
  $route = \Drupal::routeMatch()->getRouteObject();
  if ($route) {
    // Get view id & display id from current route.
    $view_id = $route->getDefault('content');
    $display_id = $route->getDefault('page_1');
    if (!empty($view_id) && !empty($display_id)) {
      // Get the view by id.
      $view = Views::getView($view_id);
      if ($view) {
        // Set display id.
        $view->setDisplay($display_id);
        // Run execute() to get result count.
        $view->execute();
        // Get view result count.
        $result_count = $view->total_rows;
      }
    }
  }
 */

	  $output = \Drupal::service('renderer')->render(views_embed_view('content', 'page_1'));

    /*  
    $block = \Drupal\block\Entity\Block::load ('block_1');
    $block_content = \Drupal::entityManager()->getViewBuilder('block')->view($block);

    return [
      '#type' => 'container',
      'element-content' => $block_content
    ];
     */

     
    $build['content'] = [
      '#markup' => $output,
    ];
    return $build;
    

    /*
    $build['content'] = [
      '#markup' => $this->t('It works!'),
    ];
    return $build;
     */
  }

  /**
   * {@inheritdoc}
   */
  protected function blockAccess(AccountInterface $account): AccessResult {
    // @todo Evaluate the access condition here.
    return AccessResult::allowedIf(TRUE);
  }

}
